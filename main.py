from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    check_label.config(text="")
    timer_label.config(text="Timer", foreground=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def Starttimer():
    global reps
    reps=reps+1
    if reps%8==0:
        countdown(LONG_BREAK_MIN)
        timer_label.config(text="BREAK",foreground=PINK)
    elif reps % 2 ==0:
        countdown(SHORT_BREAK_MIN)
        timer_label.config(text="break",foreground=RED)
    else:
        countdown(WORK_MIN)
        timer_label.config(text="WORK",foreground=RED)
#----------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min=math.floor(count/60)
    count_sec = count%60
    if math.floor(count_sec)/10 <1:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        Starttimer()
        marks=""
        for _ in range(math.floor(reps/2)):
            marks+="✓"
        check_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,105,image=tomato_img)
timer_text=canvas.create_text(103,130,text="00:00",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

timer_label=Label(text="TIMER",foreground=GREEN,bg=YELLOW,font=(FONT_NAME,22))
timer_label.grid(row=0,column=1)

start_button=Button(text="Start",background=YELLOW,command=Starttimer)
start_button.grid(row=2,column=0)

reset_button=Button(text="Reset",background=YELLOW,command=reset)
reset_button.grid(row=2,column=2)

check_label=Label(foreground=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
check_label.grid(row=2,column=1)


window.mainloop()