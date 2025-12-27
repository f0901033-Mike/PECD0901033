import tkinter as tk
from tkinter import messagebox

SIZE = 15
CELL = 30

board = [["" for _ in range(SIZE)] for _ in range(SIZE)]
current_player = "●"

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
    global current_player

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
        messagebox.showinfo("遊戲結束", f"玩家 {current_player} 獲勝！")
        root.destroy()
        return

    current_player = "○" if current_player == "●" else "●"

root = tk.Tk()
root.title("五子棋（雙人對戰）")

canvas = tk.Canvas(
    root,
    width=SIZE * CELL,
    height=SIZE * CELL,
    bg="#F5DEB3"
)
canvas.pack()

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

canvas.bind("<Button-1>", click)

root.mainloop()
