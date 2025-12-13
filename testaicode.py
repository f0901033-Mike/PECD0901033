import tkinter as tk
# 匯入 tkinter 並簡寫為 tk

import tkinter.messagebox as msg
# 測試：輸出 hello 到終端
print("hello")
# 匯入 tkinter 的訊息視窗模組 messagebox

window = tk.Tk()
# 建立主視窗物件

window.title("登入視窗")
# 設定視窗標題

window.geometry("500x400")
# 設定視窗大小

username_label = tk.Label(window, text="帳號：")
# 建立帳號標籤

username_label.pack()
# 放置帳號標籤

username_entry = tk.Entry(window)
# 建立帳號輸入框

username_entry.pack()
# 放置帳號輸入框

password_label = tk.Label(window, text="密碼：")
# 建立密碼標籤

password_label.pack()
# 放置密碼標籤

password_entry = tk.Entry(window, show="*")
# 建立密碼輸入框，使用 * 隱藏輸入

password_entry.pack()
# 放置密碼輸入框

def login():
    # 定義登入函式

    username = username_entry.get()
    # 取得帳號輸入內容

    password = password_entry.get()
    # 取得密碼輸入內容

    if username == "" or password == "":
        # 檢查帳號或密碼是否為空白

        msg.showwarning("提示", "請輸入帳號密碼")
        # 顯示警告訊息視窗

    else:
        # 若帳號密碼都有輸入
        # 建立一個新視窗顯示 hello
        top = tk.Toplevel(window)
        top.title("歡迎")
        tk.Label(top, text="hello", font=("Arial", 14)).pack(padx=20, pady=10)
        tk.Button(top, text="關閉", command=top.destroy).pack(pady=(0,10))

login_button = tk.Button(window, text="登入", command=login)
# 建立登入按鈕，按下後執行 login 函式

login_button.pack()
# 放置登入按鈕

window.mainloop()
# 啟動事件迴圈，顯示視窗
