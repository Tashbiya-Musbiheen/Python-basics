# 1....The number of times the user ask

# number=int(input("How many times you want to check?"))

# for i in range(number):
#     num=int(input(f"Enter the number {i+1}:"))
#     if num==0:
#         print("program stopped")
#         break
    
#     if num%2==0:
#         print(f" {num} It is a even number")
        
#     else:
#         print(f" {num} It is a odd number")




        
# 2..... Program to check odd/even numbers as many times as you want using for loop

# for _ in iter(int, 1):  # this creates an endless loop
#     num = int(input("Enter a number (type '0' to stop): "))
#     if num == 0:   # exit condition
#         print("Program stopped.")
#         break
#     if num % 2 == 0:
#         print(f"{num} is Even")
#     else:
#         print(f"{num} is Odd")




# 3......To print the sum of n numbers

# n=int(input("Enter n:"))
# sum=0

# for i in range(1, n+1):
#     sum=sum+i
    
# print("sum",sum)


# 4....To provide with the multiplication table

# n=int(input("Enter a num whose tables you want:"))

# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")



# 5....Factorial of a number

# n=int(input("Enter a number:"))

# fact=1

# for i in range(1,n+1):
#     fact=fact*i
    
# print(f"The factorial of {n} is",fact)
    
    
    


# 6....Even numbers between two numbers
# n=int(input("Enter start:"))
# m=int(input("Enter the end:"))

# for i in range(n,m+1):
#     if i % 2==0:
#         print(i, end=" ")
        
# print()






# 7.... while loop for printing multiplication table

# n=int(input("Enter a number:"))
# i=1

# while i<=10:
    
#     print(f"{n}*{i}={n*i}")
#     i+=1
    
    



# 8....Factorial of a number using while loop


# num=int(input("Enter a number:"))
# fact=1
# i=1

# while i<=num:
#     fact*=i
#     i+=1
# print(f"The factorial of {num} is {fact}")#here proper indentation plays a key role if the print is in for it will print the factorial from 1 to the input number is given 
# but we seek only the factorial of the given number so the print() statement should be outside the loop.







# 9....reversing a string using for loop

# text=input("Enter a string:" )
# rev=" "

# for ch in text:
#     rev=ch+rev
# print("The reverse is:",rev)
#     same thing as factorial print stmt is out of for loop only to print the last result 
    
    
    
    
    

# 10.....program to check weather the number entered is positive or negative 

# n=float(input("Enter a number:"))

# if n>0:
#     print("The number is positive")
    
# else:
#     print("The number is negative")
    
    
# even or odd

# n=int(input("Enter a number:"))

# if n % 2==0:
#     print("The number is even")
    
# else:
#     print("The number is odd")
    
    
    
# Eligible for vote 

# age=int(input("Enter the age:"))

# if age>=18:
#     print("Eligible to vote:")

# else:
#     print("Not eligible for vote")





# divisible by 5 or not

# n=int(input("Enter a number:"))

# if n % 5==0:
#     print("The number is divisible by 5")
    
# else:
#     print("The number is not divisible by 5")
    
    
    
    
    
    
# vowels are consonants

# ch=input("Enter a character:")

# if ch in 'aeiou':
#     print("Vowel")
    
# else:
#     print("Consonant")
