import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

app_label = tkinter.Label(text="Timer", font=(FONT_NAME, 28, "bold"), fg=GREEN, bg=YELLOW)
app_label.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="images/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 138, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

start_btn = tkinter.Button(text="Start")
start_btn.grid(row=2, column=0)

reset_btn = tkinter.Button(text="Reset")
reset_btn.grid(row=2, column=2)

check_mark_label = tkinter.Label(text=CHECK_MARK, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
check_mark_label.grid(row=3, column=1)


window.mainloop()
