import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import pandas as pd
import math
import random
from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import ImageTk, Image
import time
import csv

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5","Model/labels.txt")

offset = 20
imgSize = 300

counter = 0

labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q", "R",
          "S","T","U","V","W","X","Y","Z"]

character = ''

root = Tk()
root.title("SIGN RACER")
root.geometry("650x600")

#CV
def cv_creation(chat, printedw):
    while True:
        success, img = cap.read()
        imgOutput = img.copy()
        hands, img = detector.findHands(img)
        if hands:
            hand = hands[0]
            x,y,w,h = hand['bbox']

            imgWhite = np.ones((imgSize, imgSize,3),np.uint8)*255
            imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset]

            imgCropShape = imgCrop.shape
            
            aspectRatio = h/w

            if aspectRatio > 1:
                k = imgSize/h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize-wCal)/2)
                imgWhite[:, wGap:wCal+wGap] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False) 
                # print(prediction, index)

            else:
                k = imgSize/w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize-hCal)/2)
                imgWhite[hGap:hCal+hGap, :] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False)

            character = labels[index]
            wording = chat

            if character == wording.upper():
                print(character)
                printedw.append(character)
                break
                
                

            cv2.rectangle(imgOutput, (x-offset,y-offset-50), (x-offset+100, y-offset-50+50),(255,0,255),cv2.FILLED)
            cv2.putText(imgOutput, labels[index],(x,y-26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255,255,255),2)
            cv2.rectangle(imgOutput, (x-offset,y-offset), (x+w+offset, y+h+offset),(255,0,255),4)
            cv2.putText(imgOutput, ''.join(printedw), (x,y-100), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255,255,255),2)

        cv2.imshow("Image", imgOutput)
        cv2.moveWindow("Image", 650, 10)
        cv2.waitKey(1)
  
        
def start():
    input_text = user.get("1.0", "end-1c")
    WORDS = ("hack ", "side ", "physics ", "milo ","break ", "jake ", "prada ", "opver ")
    word = random.choice(WORDS)

    length_word = len(word)
    count = 0

    lbl.config(text=word[count:])
    btn.pack_forget()  # Hide the "START" button when pressed
    printedw = []
    database = []

    cap = cv2.VideoCapture(0)
    start_time = time.time()

    while count < length_word:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)

        if word[count] == ' ':
            calc_avg = 0
            lbl.config(text='')
            cap.release()
            cv2.destroyAllWindows()

            final_time = time.time() - start_time
            minutes, seconds = divmod(final_time, 60)
            hours, minutes = divmod(minutes, 60)
            final_time_format = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))

            calc_avg = round((len(word)/final_time)*10,2)

            btn.pack()
            # database.append([input_text, final_time_format])
            database.append([input_text, calc_avg])

            with open('scoreboard.csv', 'a', newline='') as file:
                wfile = csv.writer(file)
                wfile.writerows(database)

            reading = pd.read_csv('scoreboard.csv')
            print(reading)
            sorted_reading = reading.sort_values(by='SPEED', ascending=False)
            top3 = sorted_reading.head(5)

            for item in treeview.get_children():
                treeview.delete(item)

            for rank, (_, row) in enumerate(top3.iterrows(), start=1):
                treeview.insert("", "end", values=[rank] + list(row))
            treeview.pack()
            break

        cv_creation(word[count], printedw)
        count+=1
        print(count)

def on_entry_click(event):
    if user.get("1.0", "end-1c") == 'username':
        user.delete("1.0", "end-1c")  # delete all the text in the entry
        user.insert("1.0", '', 'center')  # Insert blank for user input
        user.tag_configure("center", justify = 'center')
        user.tag_add('center', '1.0', 'end')

frame_rest = Frame(root)
frame_rest.pack()
frame_img = Frame(root,pady=5)
frame_img.pack()
frame_button = Frame(root, pady=20)
frame_button.pack()
frame_score = Frame(root)
frame_score.pack()

# label creation
lbl = Label(frame_rest, text="", font=('Courier', 24))
lbl.config(fg="red")
lbl.pack(pady=20)

# custom_font = font.Font(family="Courier", size=22)
# user = Text(frame_rest, width=20, height=2, font=custom_font)
# user.insert("1.0", "username", 'center')
# user.pack()
custom_font = font.Font(family="Courier", size=22)
user = Text(frame_rest, width=20, height=2, font=custom_font)
user.pack()
# Set cursor position to the center
user.insert("1.0", "username", 'center')
# Align text to the center
user.tag_configure('center', justify='center')
user.bind("<FocusIn>", on_entry_click)



custom_font2 = font.Font(family="Courier", size=20)
btn = Button(frame_button, command=start, text="START", font=custom_font2)
btn.pack()

treeview = ttk.Treeview(root, column=("RANK", "USERNAME", "SPEED"), show="headings", height=5)

# treeview.heading("RANK", text="RANK")
# treeview.heading("USERNAME", text="USERNAME")
# treeview.heading("SPEED", text="SPEED (10e-2)")
# Set fixed width for each column
treeview.column("RANK",anchor="center")
treeview.column("USERNAME", anchor="center")
treeview.column("SPEED", anchor="center")

# Set anchor to center for each heading
treeview.heading("RANK", text="RANK", anchor="center")
treeview.heading("USERNAME", text="USERNAME", anchor="center")
treeview.heading("SPEED", text="SPEED (10e-2)", anchor="center")

style_tree = ttk.Style()
style_tree.configure("Treeview.Heading", font=('Courier', 18))
style_tree.configure('Treeview', font=("Courier", 16), rowheight=40)

reading = pd.read_csv('scoreboard.csv')

sorted_reading = reading.sort_values(by='SPEED', ascending=False)
top3 = sorted_reading.head(5)

for item in treeview.get_children():
    treeview.delete(item)

for rank, (_, row) in enumerate(top3.iterrows(), start=1):
    treeview.insert("", "end", values=[rank] + list(row))

treeview.pack()

img = Image.open('logo.jpg')
resized_img = img.resize((120,120))
img2= ImageTk.PhotoImage(resized_img)
limg = Label(frame_img, image=img2)
limg.pack()

root.mainloop()
#teachable machine google