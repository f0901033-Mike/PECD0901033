import tkinter as tk

SIZE = 15
CELL = 30
RADIUS = 12

board = [["" for _ in range(SIZE)] for _ in range(SIZE)]
current_player = "●"
game_over = False
move_history = []  # 記錄每一步 (x, y)
last_mark = None   # 上一步的紅框

def reset_game():
    global board, current_player, game_over, move_history, last_mark
    board = [["" for _ in range(SIZE)] for _ in range(SIZE)]
    current_player = "●"
    game_over = False
    move_history.clear()
    last_mark = None
    status_label.config(text="目前輪到：玩家 ●")
    canvas.delete("all")
    draw_board()

def undo():
    global current_player, game_over, last_mark
    if not move_history or game_over:
        return

    x, y = move_history.pop()
    board[x][y] = ""
    current_player = "○" if current_player == "●" else "●"
    status_label.config(text=f"目前輪到：玩家 {current_player}")
    canvas.delete("all")
    draw_board()

    for i, j in move_history:
        draw_piece(i, j, board[i][j])

def check_win(x, y, player):
    directions = [(1,0), (0,1), (1,1), (1,-1)]
    for dx, dy in directions:
        count = 1
        for d in [1, -1]:
            nx, ny = x, y
            while True:
                nx += dx * d
                ny += dy * d
                if 0 <= nx < SIZE and 0 <= ny < SIZE and board[nx][ny] == player:
                    count += 1
                else:
                    break
        if count >= 5:
            return True
    return False

def draw_piece(x, y, player):
    color = "black" if player == "●" else "white"
    cx = y * CELL + CELL // 2
    cy = x * CELL + CELL // 2
    canvas.create_oval(
        cx - RADIUS, cy - RADIUS,
        cx + RADIUS, cy + RADIUS,
        fill=color
    )

def click(event):
    global current_player, game_over, last_mark

    if game_over:
        return

    x = event.y // CELL
    y = event.x // CELL

    if x >= SIZE or y >= SIZE:
        return
    if board[x][y] != "":
        return

    board[x][y] = current_player
    move_history.append((x, y))
    draw_piece(x, y, current_player)

    # 移除舊紅框
    if last_mark:
        canvas.delete(last_mark)

    # 畫紅框標示最後一步
    cx = y * CELL + CELL // 2
    cy = x * CELL + CELL // 2
    last_mark = canvas.create_rectangle(
        cx - RADIUS - 2, cy - RADIUS - 2,
        cx + RADIUS + 2, cy + RADIUS + 2,
        outline="red", width=2
    )

    if check_win(x, y, current_player):
        status_label.config(text=f"🎉 玩家 {current_player} 獲勝！")
        game_over = True
        return

    current_player = "○" if current_player == "●" else "●"
    status_label.config(text=f"目前輪到：玩家 {current_player}")

def draw_board():
    for i in range(SIZE):
        canvas.create_line(
            CELL // 2,
            i * CELL + CELL // 2,
            SIZE * CELL - CELL // 2,
            i * CELL + CELL // 2
        )
        canvas.create_line(
            i * CELL + CELL // 2,
            CELL // 2,
            i * CELL + CELL // 2,
            SIZE * CELL - CELL // 2
        )

# ===== 視窗設定 =====
root = tk.Tk()
root.title("五子棋 版本 3（進階功能）")

status_label = tk.Label(root, text="目前輪到：玩家 ●", font=("Arial", 12))
status_label.pack(pady=5)

canvas = tk.Canvas(
    root,
    width=SIZE * CELL,
    height=SIZE * CELL,
    bg="#F5DEB3"
)
canvas.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="重新開始", command=reset_game).pack(side="left", padx=5)
tk.Button(btn_frame, text="悔棋", command=undo).pack(side="left", padx=5)

draw_board()
canvas.bind("<Button-1>", click)

root.mainloop()
