import tkinter as tk
from tkinter import messagebox

SIZE = 15
CELL = 30

board = [["" for _ in range(SIZE)] for _ in range(SIZE)]
current_player = "●"
game_over = False

def reset_game():
    global board, current_player, game_over
    board = [["" for _ in range(SIZE)] for _ in range(SIZE)]
    current_player = "●"
    game_over = False
    status_label.config(text="目前輪到：玩家 ●")
    canvas.delete("all")
    draw_board()

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

def click(event):
    global current_player, game_over

    if game_over:
        return

    x = event.y // CELL
    y = event.x // CELL

    if x >= SIZE or y >= SIZE:
        return
    if board[x][y] != "":
        return

    board[x][y] = current_player

    canvas.create_text(
        y * CELL + CELL // 2,
        x * CELL + CELL // 2,
        text=current_player,
        font=("Arial", 20)
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

# ===== 建立視窗 =====
root = tk.Tk()
root.title("五子棋 版本 2（雙人對戰）")

# 狀態文字
status_label = tk.Label(root, text="目前輪到：玩家 ●", font=("Arial", 12))
status_label.pack(pady=5)

# 棋盤畫布
canvas = tk.Canvas(
    root,
    width=SIZE * CELL,
    height=SIZE * CELL,
    bg="#F5DEB3"
)
canvas.pack()

# 重新開始按鈕
reset_button = tk.Button(root, text="重新開始", command=reset_game)
reset_button.pack(pady=5)

draw_board()
canvas.bind("<Button-1>", click)

root.mainloop()
