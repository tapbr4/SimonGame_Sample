from random import choice
from tkinter import *
from tkinter import messagebox
from sys import exit as quitgame

square = ['s1','s2','s3','s4']
s_choice = []
game = True
score = 0

def greensquare_click(event):
    squareVar.set('s1')
    greensquare.config(background = '#33cc33')
def greensquare_release(event):
    window.after(80, window.update())
    greensquare.config(background = '#196619')
    
def redsquare_click(event):
    squareVar.set('s2')
    redsquare.config(background = '#ff0000')
def redsquare_release(event):
    window.after(80, window.update())
    redsquare.config(background = '#800000')
    
def yellowsquare_click(event):
    squareVar.set('s3')
    yellowsquare.config(background = '#ffff00')
def yellowsquare_release(event):
    window.after(80, window.update())
    yellowsquare.config(background = '#808000')
    
def bluesquare_click(event):
    squareVar.set('s4')
    bluesquare.config(background = '#0066ff')
def bluesquare_release(event):
    window.after(80, window.update())
    bluesquare.config(background = '#003380')
 
# Window
window = Tk()
window.title('Simon Game Sample')
window.resizable(width = False, height = False)
squareVar = StringVar()

topframe = Frame(window, height=150,width=300)
greensquare = Frame(topframe, bg='#196619', height=150,width=150)
greensquare.bind('<Button-1>',greensquare_click)
greensquare.bind('<ButtonRelease-1>', greensquare_release)
redsquare = Frame(topframe, bg='#800000', height=150,width=150)
redsquare.bind('<Button-1>',redsquare_click)
redsquare.bind('<ButtonRelease-1>', redsquare_release)

botframe = Frame(window, height=150,width=300)
yellowsquare = Frame(botframe, bg='#808000', height=150,width=150)
yellowsquare.bind('<Button-1>',yellowsquare_click)
yellowsquare.bind('<ButtonRelease-1>', yellowsquare_release)
bluesquare = Frame(botframe, bg='#003380', height=150,width=150)
bluesquare.bind('<Button-1>',bluesquare_click)
bluesquare.bind('<ButtonRelease-1>', bluesquare_release)

topframe.pack(side='top')
botframe.pack(side='bottom')
greensquare.pack(side='left')
redsquare.pack(side='left')
yellowsquare.pack(side='left')
bluesquare.pack(side='left')

startgame = messagebox.askyesno('Start Game', 'Start a new game?')
if startgame:
    while game:
        rand = choice(square)
        s_choice.append(rand)
        
        for i in range(len(s_choice)):
            if s_choice[i] == 's1':
                greensquare.config(background = '#33cc33')
                window.after(500, window.update())
                greensquare.config(background = '#196619')
                window.after(800, window.update())
            elif s_choice[i] == 's2':
                redsquare.config(background = '#ff0000')
                window.after(500, window.update())
                redsquare.config(background = '#800000')
                window.after(800, window.update())
            elif s_choice[i] == 's3':
                yellowsquare.config(background = '#ffff00')
                window.after(500, window.update())
                yellowsquare.config(background = '#808000')
                window.after(800, window.update())
            else:
                bluesquare.config(background = '#0066ff')
                window.after(500, window.update())
                bluesquare.config(background = '#003380')
                window.after(800, window.update())
                
        for i in range(len(s_choice)):
            window.wait_variable(squareVar)
            if s_choice[i] == squareVar.get():
                pass
            else:
                confirm = messagebox.showinfo('GameOver',f'Your score: {score}')
                if confirm:
                    game = False
                    window.destroy()
                    quitgame()
                         
        window.after(500, window.update())
        greensquare.config(background = '#196619')
        redsquare.config(background = '#800000')
        yellowsquare.config(background = '#808000')
        bluesquare.config(background = '#003380')
        window.after(800, window.update())
        
        score += 1
        print(f'Score: {score}')
            
else:
    window.destroy()

window.mainloop()
