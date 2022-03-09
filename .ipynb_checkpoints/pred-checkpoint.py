# UNREADABLE CODE :) by Sarzil

import tkinter, os, numpy as np
from PIL import Image, ImageTk, ImageOps
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

model = tf.keras.models.load_model("DigiPredictor04.h5")

def main():
    app = tkinter.Tk()
    app.geometry("400x400")
    app.title("Write a number between 0 and 9")

    def get_x_and_y(event):
        global lasx, lasy
        lasx, lasy = event.x, event.y

    def draw(event):
        global lasx, lasy
        canvas.create_line((lasx, lasy), event.x, event.y, fill='white', width=14)
        lasx, lasy = event.x, event.y

    canvas = tkinter.Canvas(app, bg="black")
    canvas.pack(anchor='nw', fill='both', expand=1)
    canvas.bind("<Button-1>", get_x_and_y)
    canvas.bind("<B1-Motion>", draw)

    def predict():

        canvas.postscript(file="tmp.ps", colormode='color')
        img = ImageOps.grayscale(Image.open("tmp.ps").resize((28,28)))
        im = np.array(img).reshape(1,28,28,1).astype("float32") / 255.0
        out = model.predict(im)
        print("\nYou typed: {}".format(int(tf.math.argmax(out[0]))))
        app.destroy()
        main()

    predict_button = tkinter.Button(app, text = "Predict", command = predict)
    predict_button.pack()

    img = Image.new("RGB", (400,400), color='black')
    image = ImageTk.PhotoImage(img)
    canvas.create_image(0,0, image=image, anchor='nw')                  

    app.mainloop()

main()









