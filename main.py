from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pandas
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import math

l_time = []
list1 = []
l_score = []


def openfile():
    global list1
    global l_time
    user = filedialog.askopenfilename()
    with open(user, "r") as user_t:
        u_data = pandas.read_csv(user_t)
        user_pitch_list = u_data["User Pitch(Hz)"].to_list()
        final_user_list = [item for item in user_pitch_list if not (pandas.isnull(item)) == True]
        list1.append(final_user_list)
        trainers_pitch_list = u_data["Trainer Pitch(Hz)"].to_list()
        final_trainers_list = [item for item in trainers_pitch_list if not (pandas.isnull(item)) == True]
        list1.append(final_trainers_list)
        time_list = u_data["Current Timestamp"].to_list()
        final_time_list = [item for item in time_list if not (pandas.isnull(item)) == True]
        l_time.append(final_time_list)
        score = u_data["Score"].to_list()
        final_score = [item for item in score if not (pandas.isnull(item)) == True]
        l_score.append(final_score)

        return user_pitch_list


# --------------------------------------------------SCORE------------------------------------------------------------------------------
def calc_score():
    l_s = l_score[0]
    total = float(0)
    a = len(l_s)
    for i in range(a):
        total += l_s[i]

    percentage_score = (total / (a * 100)) * 100
    score_label.config(text=math.floor(percentage_score))


l1 = []
l2 = []


def create_graph():

    fig = plt.Figure(figsize=(6, 5), dpi=100)
    frame1 = Frame(second_frame, pady=20, padx=20, bg="azure")
    plot = fig.add_subplot(111)
    l1.append(list1[0])
    l1.append(list1[1])
    for i in range(len(l1)):
        c = ["red", "blue", "green"]
        y = l1[i]
        x = l_time[0]
        col = c[i]
        plot.plot(x, y, color=col)

    plot.set_title("timestamp-user pitch graph")
    plot.set_xlabel("timestamps")
    plot.set_ylabel("user pitch frequency")
    canvas1 = FigureCanvasTkAgg(fig, master=second_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas1, frame1)
    toolbar.config(bg="azure")
    toolbar.pack()
    frame1.pack()

    fig1 = plt.Figure(figsize=(6, 5), dpi=100)
    frame2 = Frame(second_frame, padx=20, pady=20, bg="azure")
    plot2 = fig1.add_subplot(211)
    l2.append(l_score[0])
    x = l_time[0]
    y = l2[0]
    plot2.plot(x, y, color="g")
    plot2.set_title("timestamp-score graph")
    plot2.set_xlabel("timestamps")
    plot2.set_ylabel("score")
    canvas2 = FigureCanvasTkAgg(fig1, master=second_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack()
    toolbar2 = NavigationToolbar2Tk(canvas2, frame2)
    toolbar2.config(bg="azure")
    toolbar2.pack()
    frame2.pack()


# ------------------------------------------GUI----------------------------------------------------#
window = Tk()
window.title("MUSIC AI")
window.minsize(width=700, height=700)
window.config(bg="white", padx=10, pady=10)

main_frame = Frame(window, bg="azure")
main_frame.pack(fill=BOTH, expand=1)

canvas = Canvas(main_frame, bg="azure")
canvas.pack(side=LEFT, fill=BOTH, expand=1)
scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
second_frame = Frame(canvas, bg="azure")
canvas.create_window((0, 0), window=second_frame, anchor="nw")

user_audio_label = Label(second_frame, text="MUSIC", font=("arial", 14,), bg="azure")
user_audio_label.pack()

button = ttk.Button(second_frame, text="browse a csv file", command=openfile)
button.pack()

button1 = Button(second_frame, text="calculate score", command=calc_score)
button1.pack()

score_label = Label(second_frame, text="score", font=("arial", 14,), bg="azure")
score_label.pack()

button2 = Button(second_frame, text="create graph", command=create_graph)
button2.pack()

window.mainloop()
