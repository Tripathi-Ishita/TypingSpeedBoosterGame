words=['Sugar','Icecream','Tinkerbell','Muffin','Money','Love','Affection','Honey','Sugarplum','Litchi',
       'Felicity','Kookie','World','Rainbow','Friends','College','Country','Intelligent','Indians','Koreans'
       ,'Diary','Innocent','Japanese','Ramen','Noodles','Kimchi','Fictions','Frozen','Cherry','Hawaii']

def labelslider():
    global count,sliderword
    text='WELCOME TO TYPING SPEED BOOSTER'
    if(count>=len(text)):
        count=0
        sliderword=''
    sliderword+=text[count]
    count+=1
    fontLabel.configure(text=sliderword)
    fontLabel.after(150,labelslider)#calls labelslider ahter 1000 microsec

def time():
    global timeleft,score,miss
    if(timeleft>=11):
        pass
    else:
        timeLabelCount.configure(fg='red')
    if (timeleft>0):
        timeleft-=1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)
    else:#for showing scores
        gamePlayDetailLabel.configure(text='Hit = {}| Miss = {}|Total Score = {}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('Notification:', 'HIT ENTER TO RESTART GAME')
        if (rr==True):
            score=0
            timeleft=60
            miss=0
            timeLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)
#######string main kuch alg se type krna hai to format,curly brace lagkr value

# ####################################startgame
def startGame(Event):
    global score,miss
    if(timeleft==60):
        time()
    gamePlayDetailLabel.configure(text='')#ek bar enter press kremge toh niche wala line delte ho jayega(hit and press enter wala)
    if(wordEntry.get()==wordLabel['text']):
        score+=1
        scoreLabelCount.configure(text=score)

    else:
        miss+=1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    print(wordEntry.get())
    wordEntry.delete(0,END)


#to create a box
from tkinter import *
import random
from tkinter import messagebox
#to get words randomly
root=Tk()
root.geometry('700x500+300+70')#300 from left shift and 70 from bottom shift
root.configure(bg='mistyrose1')
root.title('Typing Speed Booster Game')
################################varaiable
score=0
timeleft=60
count=0
sliderword=''
miss=0
########################################label
fontLabel=Label(root,text='',font=('Century Gothic',26,' italic bold')
                ,bg='yellow',fg='blue',width=30)
#text style,text sixe,text bold
fontLabel.place(x=40,y=15)
labelslider()
random.shuffle(words)#jitni bar call hoga,utni bar words randomly cal hoga
wordLabel=Label(root,text=words[5],font=('Century Gothic',35,' italic bold'),bg='mistyrose1')
wordLabel.place(x=280,y=200)


scoreLabel=Label(root,text='Your Score:',font=('Century Gothic',25,' italic bold'),bg='mistyrose1',)
scoreLabel.place(x=10,y=90)#yourscore palce ho gya
scoreLabelCount=Label(root,text=score,font=('Century Gothic',25,' italic bold'),bg='mistyrose1',fg='blue')
scoreLabelCount.place(x=85,y=150)

timerLabel=Label(root,text='Time Left:',font=('Century Gothic',25,' italic bold'),bg='mistyrose1',)
timerLabel.place(x=500,y=90)

timeLabelCount=Label(root,text=timeleft,font=('Century Gothic',25,' italic bold'),bg='mistyrose1',fg='blue')
timeLabelCount.place(x=550,y=150)
gamePlayDetailLabel=Label(root,text='Type Word And Hit Enter Button',font=('arial',30,'italic bold')
                          ,bg='mistyrose1',fg='brown')
gamePlayDetailLabel.place(x=50,y=400)


#######################################entry of words
wordEntry=Entry(root,font=('Century Gothic',25,' italic bold'),border=10,justify='center')#word entry at box
wordEntry.place(x=170,y=300)#box position
wordEntry.focus_set()#bich main arrow ko lane k liye jissse bina click kie type ho
#######################################funtio
root.bind('<Return>',startGame)#shows enetr buutons,binds enter button to this program

root.mainloop()