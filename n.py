# # N = input('enter input string:').lower()
# # order = 'abcdefghijklmnopqrstuvwxyz'
# # rev = 'zyxwvutsrqponmlkjihgfedcba'
# # dic = dict(zip(order,rev))
# # mirror = ''
# # for i in range(len(N)):
# #   mirror = mirror + dic[N[i]]

# # string_1 = "Program"
# # string_2 = string_1[::-1]
# # print(string_2)

# # from tkinter import *
# # import math as m

# # root = Tk()
# # root.title('simple calculator')
# # e=Entry(root,width=50,borderwidth=5,fg='white',bg='black')
# # e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

# # def click(to_print):
# #   old = e.get()
# #   e.delete(0, END)
# #   e.insert(0, old+to_print)
# #   return

# # def sc(event):
# #   key=event.widget
# #   text=key['text']
# #   no = e.get()
# #   result = ''

# #   if text == 'log':
# #     result=str(m.log10(float(no)))
# #   e.delete(0, END)
# #   e.insert(0, result)



# # lo=Button(root,padx=10,pady=10,text='log',relief=RAISED, bg="Black", fg="White")
# # lo.bind("<Button-1>", sc)
# # lo.gr
# # root.mainloop()


# ### Hangman Game Project 

# # Hangman game is just a word guessing game by guess the character of the word. In this game, there is a list of words present, out of which our interpreter will choose 1 random word.

# # The user first has to input their names and then, will be asked to guess any alphabet. If the random word contains that alphabet, it will be shown as the output(with correct placement) else the program will ask you to guess another alphabet. Users will be given 10 turns(can be changed accordingly) to guess the complete word.

# ### TODO
# # Change the turns that you want to give the player
# # Change the list containing Secret word list



# from os import system
# import random

# def cls():
#     system ('cls')

# def hangman_game():
#     cls()
    
#     print("\nWelcome")
#     print("Lets play Hangman\n")

#     name = input("What is your name?")
#     name = name.capitalize()
#     print("Hello " + name + ", It is time to play HamgMan")
#     print("Start Guessing...")
#     guessed_word = []

#     # Creats a variable with an empty value
#     guesses = ""

#     # Determine the Number of turns
#     turns = 10                                  #ToDo : Change the turns that you want to give the player

#     # Here we set the Secret
#     words = [
#         "Forrest Gump",
#         "Hangman Project",
#         "The Godfather",
#         "The Green Mile",
#         "Hotel Rwanda",
#         "Goodfellas",
#         "Scarface",
#         "The Terminal",
#         "Million Dollar Baby",
#         "Driving Miss Daisy",
#         "Catch Me If You Can",
#         "Chinatown",
#         "The Departed",
#         "Dances with Wolves",
#         "Ford v Ferrari",
#         "Little Women",
#         "A Star Is Born",
#         "Dear Basketball"
#     ]

#     word = random.choice(words)
#     word = word.upper()

#     while turns > 0:
#         failed = 0

#         for char in word:
#             if char in guesses:
#                 print(char, end=" ")

#             elif char == " ":
#                 print(' / ', end=" ")
                
#             else:
#                 print("_", end=" ")
#                 failed += 1

#         if failed == 0:
#             print("\n" + name + " you WON!     :)")
#             break

#         guess = input("\nGuess a Character : ")
#         guess = guess.upper()

#         if len(guess) > 1:
#             break

#         guesses += guess
#         if (guess not in word) and (guess not in guessed_word):
#             turns -= 1
#             guessed_word.append(guess)
#             print("\nWrong Guess :/")
#         cls()

#         print("\nYou have ", + turns, "more guesses")
#         print("\nWrong Character's Entered : ", guessed_word)

#         if turns == 0:
#             print("\nGame is OVER, you LOST :o")

#     check = input("\nDo you want to play again Y/N?")

#     if check == "Y" or check == "y" :
#         hangman_game()


# hangman_game()


from tkinter import *
import datetime
import time
import os

root=Tk()
def alarm(set_alarm):
    while True:
        time.sleep(1)
        current_time=datetime.datetime.now().time()
        current_time = str(current_time)
        current_time = current_time[:5]
        if current_time==set_alarm:
            print("Time to wake up")
            os.system("start HeyYa.mp3")

            break

def actual_time():
    set_alarm=f"{hour.get()}:{minute.get()}"
    set_alarm=str(set_alarm)
    alarm(set_alarm)



root.title("Alarm clock")
root.geometry("350x200")

hour=StringVar()
minute=StringVar()
Label(root,text="Hours   Min",font="bold").place(x=10)


hourTime=Entry(root,textvariable=hour,bg="lightblue",fg="black",font="Arial",width=5).place(x=10,y=30)
minuteTime=Entry(root,textvariable=minute,bg="lightblue",fg="black",font="Arial",width=5).place(x=50,y=30)
Label(root,text="Enter time in 24 hour format.",bg="pink",fg="black",font="Arial").place(x=10,y=120)
set=Button(root,text="Set alarm",fg="black",width=10,command=actual_time).place(x=10,y=70)

root.mainloop()