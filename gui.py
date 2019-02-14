from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import pandas as pd
import numpy as np
from predict import *

class UI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.width= 900
        self.height= 500
        self.canvas = Canvas(self, width = self.width, height = \
        self.height)
        self.canvas.pack()
        self.info= PhotoImage(file='img/info.png')
        self.coverScreen()

    def coverScreen(self):
        self.canvas.delete('all')
        self.start = Image.open('img/pa.png')
        self.startImg = ImageTk.PhotoImage(self.start)
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill="white")
        self.canvas.create_image(self.width/2, self.height/3*2, \
        image=self.startImg)
        self.canvas.create_text(self.width/2, self.height/5, \
        text="Drug Abuse Detection System", fill="black", font=("ms serif", 48, "bold"))
        self.startButton = Button(self, text="Start", \
        command=self.about, width= 10)
        self.startButton.config(font=('ms serif', 12))
        self.canvas.create_window(self.width/2, self.height/10*9, \
        window=self.startButton)

    def about(self):
        self.canvas.delete('all')
        self.aboutImg = Image.open('img/about.jpg')
        self.tkabout = ImageTk.PhotoImage(self.aboutImg)
        self.canvas.create_image(self.width/2, self.height/2, \
        image=self.tkabout)
        self.backSelect= Button(self, command= self.coverScreen, text= 'Back')
        self.backSelect.config(width=10)
        self.canvas.create_window(self.width/12, self.height/15, window= self.backSelect)

        self.continueButton = Button(self, text="Continue", \
        command=self.enter, width= 10)
        self.continueButton.config(font=('ms serif', 12))
        self.canvas.create_window(self.width/3*2, self.height/10*9, \
        window=self.continueButton)

    def enter(self):
        self.canvas.delete('all')
        self.drug = Image.open('img/opiod.png')
        self.pdrug = ImageTk.PhotoImage(self.drug)
        self.canvas.create_image(self.width/2, self.height/2, \
        image=self.pdrug)
        self.canvas.create_text(self.width/5*4, self.height/3*2, \
        text="Data File Upload", fill="white", font=("ms serif", 30, "bold"))

        self.up= Button(self, command= self.fileEntry)
        self.scriptImg= Image.open('img/prescribe.png')
        self.tksImg= ImageTk.PhotoImage(self.scriptImg)
        self.up.config(image=self.tksImg, compound=CENTER, width= 300, height=150)
        self.canvas.create_window(self.width/5*4, self.height/3, window= self.up)

        self.backSelect= Button(self, command= self.about, text= 'Back')
        self.backSelect.config(width=10)
        self.canvas.create_window(self.width/12, self.height/15, window= self.backSelect)

        self.iButton= Button(self, command=self.instruct)
        self.iButton.config(image=self.info, compound= CENTER, width=30, height=30)
        self.canvas.create_window(self.width/15, self.height/10*8, window= self.iButton)

    def instruct(self):
        self.canvas.delete('all')
        self.help1 = Image.open('img/instruct1.jpg')
        self.tkhelp1 = ImageTk.PhotoImage(self.help1)
        self.canvas.create_image(self.width/2, self.height/2, image=self.tkhelp1)

        self.tkexit= PhotoImage(file='img/exit.png')
        self.tknext= PhotoImage(file='img/next.png')
        self.exit= Button(self, command=self.enter)
        self.exit.config(image= self.tkexit, compound= CENTER)
        self.canvas.create_window(self.width/20*19, self.height/12, window= self.exit)
        self.next= Button(self, command=self.instruct2)
        self.next.config(image= self.tknext, compound= CENTER)
        self.canvas.create_window(self.width/20*19, self.height/12*11, window= self.next)


    def instruct2(self):
        self.canvas.delete('all')
        self.help2 = Image.open('img/instruct2.jpg')
        self.tkhelp2 = ImageTk.PhotoImage(self.help2)
        self.canvas.create_image(self.width/2, self.height/2, image=self.tkhelp2)
        self.tkexit= PhotoImage(file='img/exit.png')
        self.tkprev= PhotoImage(file='img/previous.png')
        self.exit= Button(self, command=self.enter)
        self.exit.config(image= self.tkexit, compound= CENTER)
        self.canvas.create_window(self.width/20*19, self.height/12, window= self.exit)
        self.previous= Button(self, command=self.instruct)
        self.previous.config(image= self.tkprev, compound= CENTER)
        self.canvas.create_window(self.width/20*19, self.height/12*11, window= self.previous)



    def fileEntry(self):
        # open csv file, read in dataframe
        # add predictions to df then save it as new file
        self.file =  filedialog.askopenfilename(initialdir = "/", \
        title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        if self.file != None:
            data = pd.read_csv(self.file)
            data=data[extractFeatures()]
            valList=list()
            for i, row in data.iterrows():
                val= returnPreds([np.array(data.iloc[i])])
                if val==1:
                    val = "Pill Mill"
                else:
                    val= "Not Pill Mill"
                valList.append(val)
            v= pd.Series(valList)
            data['preds']= v.values
            data.to_csv('predictions.csv')
            print('done')

        self.canvas.delete('all')
        self.done = Image.open('img/done.jpg')
        self.tkdone= ImageTk.PhotoImage(self.done)
        self.canvas.create_image(self.width/2, self.height/2, image= self.tkdone)

        self.back= Button(self, command= self.enter, text= 'Back')
        self.back.config(width=10)
        self.canvas.create_window(self.width/12, self.height/15, window= self.back)



predUI = UI()
predUI.mainloop()
