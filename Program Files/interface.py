from tkinter import *
from pynput.keyboard import Key, Controller



# # Type a lower case A; this will work even if no key on the
# # physical keyboard is labelled 'A'
# keyboard.press('a')
# keyboard.release('a')

# # Type two upper case As
# keyboard.press('A')
# keyboard.release('A')
# with keyboard.pressed(Key.shift):
#     keyboard.press('a')
#     keyboard.release('a')

# # Type 'Hello World' using the shortcut type method
# keyboard.type('Hello World')
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
    def gotoDesktop():
        print("hello")
        keyboard = Controller()
        
        keyboard.press(Key.cmd_l)
        keyboard.press('d')
        keyboard.release('d')
        keyboard.release(Key.cmd_l)
            
    

    img4=PhotoImage(file='option1.png')
    op1=Button(window,image=img4,borderwidth=0,bg='black',command=gotoDesktop)
    op1.place(x=650,y=350)

    img5=PhotoImage(file='option2.png')
    op2=Button(window,image=img5,borderwidth=0,bg='black')
    op2.place(x=655,y=450)
    


    
    
    window.configure(bg='black');

    
    window.mainloop()











if __name__=='__main__':
    main()