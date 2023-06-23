import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

cap = cv2.VideoCapture('opencv/data/vtest.avi')

fig = plt.figure(figsize)



def init():
    global im
    retval frame = cap.read()
    im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_B))


def updateFrame(k):
    retval, frame = cap.read()
    if retval:
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))


animation.FuncAnimation(fig,updateFrame, init_func=init, interval=50)

while True:
    fig.canvas.draw()
    fig.canvas.flush_events()

if cap.isOpened():
    cap.release
