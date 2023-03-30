from tkinter import *
from pynput.keyboard import Key, Controller
import core


def main():    
    




    window =Tk()   
    window.title("HCI MK1")
    window.geometry('1920x1080')

    

    #logo
    img1=PhotoImage(file='team_logo.png')
    logo=Label(window,image=img1,bg='black')
    logo.place(x=50, y=50)

    #title
    img2=PhotoImage(file='title.png')
    title=Label(window,image=img2,bg='black')
    title.place(x=650,y=80)

    #chooseinterface
    img3=PhotoImage(file='int.png')
    int=Label(window,image=img3,bg='black')
    int.place(x=50, y=250)

    # #options

    def scroll(flag):
        flag=True
        while flag:
            core.core(1)
    
            
        
            
    

    img4=PhotoImage(file='option1.png')
    op1=Button(window,image=img4,borderwidth=0,bg='black',command=scroll(True))
     
    op1.place(x=650,y=350)

    img5=PhotoImage(file='option2.png')
    op2=Button(window,image=img5,borderwidth=0,bg='black')
    op2.place(x=650,y=450)

    img6=PhotoImage(file='option3.png')
    op3=Button(window,image=img6,borderwidth=0,bg='black')
    op3.place(x=650,y=550)

   
    


    
    
    window.configure(bg='black');
    

    
    window.mainloop()
    


     











if __name__=='__main__':
    main()