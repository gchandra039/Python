# a = "the list the page list of package"
# def str_words(str):
#   words = str.split()
#   count = dict()
#   for word in words:
#     if word in count:
#       count[word] += 1
#     else:
#       count[word] = 1
#   return count
# print(str_words(a))

#####################

# def fib(n):
#   if n == 1 or n == 2:
#     return 1
#   else:
#     return (fib(n-1) + fib(n-2))

# print(fib(3))

########################

# a = float(input("enter value: "))
# if a > 0:
#   print("positive")
# else:
#   print("negitive")

###################

# n = int(input("enter value: "))
# s = n
# b = len(str(n))
# sum = 0
# while n != 0:
#   r = n%10  #153%10 = 3  15%10 = 5
#   sum = sum + (r**b)  # 0+(3**3)+(5**3)+(1**3)
#   n = n//10  #153//10 = 15 repeat loop   
# if s == sum:
#   print("armstong number")
# else:
#   print("not")

#######################################

# my_string = input("enter the string: ")
# l = int(len(my_string))
# n = 0
# for i in my_string:
#     print(my_string[0:n])
#     n += 1
# for i in my_string:
#   print(my_string[0:l])
#   l -= 1

##############################################

# r = 6
# for i in range(r):
#   for j in range(i+1):
#     print(i,end=" ")
#   print(" ")

######################

# r = 6
# for i in range(r):
#   for j in range(i+1):
#     print("*",end=" ")
#   print(" ")


#################

# l1 = [0,2,5,1]
# str1 = "7"
# for i in l1:
#   str1 = str1 + i
# print(str1)

##################

# def modify_list(my_list):
#       my_list[0] = 99
#       my_list = [1,2,3]
# num = [4,5,6]
# modify_list(num)
# print(num)

#####################

# import calendar
# year = 2023
# print(calendar.calendar(int(year)))


##########################

# str = input("enter the str: ")
# rev = str[::-1]
# print(rev)

#####################

# s = input("enter string: ")
# l = len(s)-1
# output = ""
# while l >= 0:
#   output = output + s[l]
#   l = l-1
# print(output)


from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root=Tk()
root.title("Air quality detector")
#root.iconbitmap('c:/Users/Garima Singh/Desktop/image.png')
root.geometry("800x40")
root.configure(background='green')

try:
	api_request= requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=10&API_KEY=1415D85E-FB89-40EF-B8F0-63F99A595BC8")
	api=json.loads(api_request.content)
	city=api[0]['ReportingArea']
	quality=api[0]['AQI']
	category=api[0]['Category']['Name']
except Exception as e:
	api="Error..."

myLabel= Label(root, text=city + " Air Quality" + str(quality) + " "+ category, font=("Helvetica", 20), background="green")
myLabel.pack()


root.mainloop()