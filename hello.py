#Develop a software to calculate sales
#1)Ask name of the user
#2)Ask for how many percent is the sales tax
#3)The output : "Hi, xxxx, the amount to pay is xxx, the sales is xxx "
#sales amount = total sales + sales tax
#Barang = Rm1,500 tax 6.25%, total amount = 1631.25

#name = input("What is your name?\n")
#goods = float(input ("How many is the amount to pay?\n"))
#tax = float(input ("How many percent is the sales tax?\n"))
#salesTax = tax/100 * goods
#salesAmount = salesTax + goods
#print("Hi " + name + ", the total amount to pay is RM" + str(salesAmount))

#c-f

#name = input("What is your name?\n")
#celsius = float(input("What is your temperature in celsius?\n"))
#farenheit = (celsius * 1.8) + 32
#print("The temperature in farenheit is : " + str(farenheit))

#name1 = input("What is your name?\n")
#name2 = input("What is your name?\n")

#temperature = float(input("What is the temperature today?\n"))
#if temperature > 80 :
#    print("It's too hot!")
#    print("Stay Inside")
#elif temperature > 55 :
#    print("Still quite hot!")  
#print("Have a nice day")

name = input("What is your name?\n")
mark = float(input("Hi " + name + ", what is your mark?\n"))
if mark >= 80 :
    print("Hi " + name + ", your mark is " + str(mark) + ", you are brilliant!")
elif mark <= 60 :
    print("Hi " + name + ", your mark is " + str(mark) + ", you did okay")
    print("Better luck next time :)")
