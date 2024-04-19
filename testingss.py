
from tkinter import *
import cv2 
from PIL import Image, ImageTk

from app import vid

cap = cv2.VideoCapture(0)

def open_camera():

	# Capture the video frame by frame
	_, frame = vid.read()

	# Convert image from one color space to other
	opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

	# Capture the latest frame and transform to image
	captured_image = Image.fromarray(opencv_image)

	# Convert captured image to photoimage
	photo_image = ImageTk.PhotoImage(image=captured_image)

	# Displaying photoimage in the label
	label_widget.photo_image = photo_image

	# Configure image in the label
	label_widget.configure(image=photo_image)

	# Repeat the same process after every 10 seconds
	label_widget.after(10, open_camera)

width, height = 400,400
# Width of camera, #Height of Camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

app = Tk()
app.bind('<Escape>', lambda e: app.quit())

label_widget = Label(app)
label_widget.pack()

button1 = Button(app, text="Open Camera",
				command=open_camera)
button1.pack()