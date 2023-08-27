from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pandas
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

l_time = []
list1 = []


def openfile():
    global list1
    global l_time
    user = filedialog.askopenfilename()
    with open(user, "r") as user_t:
        u_data = pandas.read_csv(user_t)
        user_pitch_list = u_data["User Pitch(Hz)"].to_list()
        final_user_list = ew_list = [item for item in user_pitch_list if not (pandas.isnull(item)) == True]
        l1.append(final_user_list)
        trainers_pitch_list = u_data["Trainer Pitch(Hz)"].to_list()
        final_trainers_list = ew_list = [item for item in trainers_pitch_list if not (pandas.isnull(item)) == True]
        l1.append(final_trainers_list)
        time_list = u_data["Current Timestamp"].to_list()
        final_time_list = [item for item in time_list if not (pandas.isnull(item)) == True]
        l_time.append(final_time_list)

        return user_pitch_list



l1 = []


def create_graph():
    fig = plt.Figure(figsize=(6, 5), dpi=100)
    plot = fig.add_subplot(111)
    l1.append(list1[0])
    l1.append(list1[1])
    for i in range(len(l1)):
        print(list1[i])
        print(l_time[0])
        c = ["red", "blue", "green"]
        y = l1[i]
        x = l_time[0]
        col = c[i]
        plot.plot(x, y, color=col)

    plot.set_title("timestamp-user pitch graph")
    plot.set_xlabel("timestamps")
    plot.set_ylabel("user pitch frequency")
    canvas = FigureCanvasTkAgg(fig, master=second_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, second_frame)
    toolbar.update()
    toolbar.pack()




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

button = ttk.Button(second_frame, text="browse file", command=openfile)
button.pack()

button1 = Button(second_frame, text="create graph", command=create_graph)
button1.pack()

window.mainloop()
