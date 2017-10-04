from Tkinter import *
import os
import sys
#ip = sys.argv[2]

root = Tk()

def forward():
    print "forward"
    ip = ipEntry.get()
    f = os.popen('ssh pi@'+ip+' python ~/python_scripts/forward.py')


def backward():
    print "backward"
    ip = ipEntry.get()
    f = os.popen('ssh pi@'+ip+' python ~/python_scripts/backwards.py')


def left():
    print "left"
    ip = ipEntry.get()
    f = os.popen('ssh pi@'+ip+' python ~/python_scripts/left.py')


def right():
    print "right"
    ip = ipEntry.get()
    f = os.popen('ssh pi@'+ip+' python ~/python_scripts/right.py')




ipEntry = Entry(root)
button_forward = Button(root, text="forward", command=forward)
button_backward = Button(root, text="backward", command=backward)
button_left = Button(root, text="left", command=left)
button_right = Button(root, text="right", command=right)




ipEntry.pack()
button_forward.pack(side=TOP)
button_left.pack(side=LEFT)
button_right.pack(side=RIGHT)
button_backward.pack(side=BOTTOM)
root.mainloop()