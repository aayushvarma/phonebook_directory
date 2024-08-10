import pandas as pd 
import doctest
import csv
import sys as sys
from doctest import testmod
df1=pd.read_csv(r"D:\Praveen Varma\Documents\Book2.csv")
df2=pd.read_csv(r"D:\Praveen Varma\Documents\Book3.csv")
df3=pd.read_csv(r"D:\Praveen Varma\Documents\Book1.csv")
df4=pd.read_csv(r"D:\Praveen Varma\Documents\Book4.csv")
df5=pd.read_csv(r"D:\Praveen Varma\Documents\Book5.csv")
df6=pd.read_csv(r"D:\Praveen Varma\Documents\Book6.csv")
df7=pd.read_csv(r"D:\Praveen Varma\Documents\Book7.csv")
df8=pd.read_csv(r"D:\Praveen Varma\Documents\Book8.csv")
def physics():
    phy=input("Enter P for Physics cycle.")
    if phy=="p" or phy=="P":
        print("Welcome to Physics cycle.")
        print("***************************")
        print('''Enter 1 to view your subjects.
Enter 2 to view CS teachers
      3 to view Math teachers
      4 to view other teachers
      5 to view additonal faculty
      6 to exit the program.''')
        while True:
            ncr=int(input("Enter number:"))
          
            if ncr==1:
               print(df6)
               break
            elif ncr==2:
               print(df1)
               break
            elif ncr==3:
               print(df3)
               break  
            elif ncr==4:
               print(df7)
               break
            elif ncr==5:
               print(df8)
               break
            elif ncr==6:
               print("You are now exiting the program.")
               sys.exit()
               break
            else:
               print("Wrong number!Try again.")
            
    else:
        print('Invalid Option! Please try again.')

        
        
cstr="CONTACT PANEL-PESU"
print("***********************************************************************")
print(cstr.center(64)) 
print("***********************************************************************")
print()
while True:
    srn=input("Enter class roll no.-")
    if len(srn)==3:
        break    
    else:
        print("Only 3 characters are allowed")
while True:
    year=input("Enter year of joining-")
    if len(year)==4:
        break    
    else:
        print("Only 4 characters are allowed")
while True:        
    campus=input("Enter 1 for RR campus & 2 for EC campus-")
    if campus=="1" or campus=="2":
        break
    else:
        print("Only 1 or 2 can be entered.")
        
print()
print('''1 for CSE
2 for ECE
3 for EEE
4 for MECH
5 for BIO''')
while True:
    branch=int(input("Enter your branch code-"))
    if branch==1:
        b='CS'
        break
    elif branch==2:
        b='EC'
        break
    elif branch==3:
        b='EE'
        break 
    elif branch==4:
        b='ME'
        break
    elif branch==5:
        b='BT'
        break
        
    else:
        print('Invalid Option! Please try again.')
list1=['PES',campus,'UG',year[-2:],b,srn]
print("**")
print("Your SRN is:")
print("".join(list1))

if campus=="1":
    print("****************************")
    print("Sorry, RR Campus Directory does not exist.")
    sys.exit()                  
    
    
if branch==3 or branch==4 or branch==5:
    print("****************************")
    print("Error! You are not from EC Campus")
    sys.exit()
while True:
    xyz=input("To view EC Campus directory enter E.")
    if xyz=="e" or xyz=="E":
        print("Welcome to EC Campus directory.")
        break
    else:
        print("Please try again.")
if branch==1:
    print('You are in Computer Science Engineering.')
    print("*******************") 
elif branch==2:
    print('You are in Electronics & Communication Engineering.')
    print("*******************")
while True:
    chm=input("Enter C for Chemistry cycle.")
    if chm=="c" or chm=="C":
        print("Welcome to Chemistry cycle.")
        print("***************************")
        print('''Enter 1 to view your subjects.
Enter 2 to view CS teachers
      3 to view Math teachers
      4 to view other teachers
      5 to view additonal faculty
      6 to go to Physics cycle''')
        nbr=1
        while nbr<6:
            nbr=int(input("Enter number:"))
            if nbr==1:
                print(df2)
                break
            elif nbr==2:
                print(df1)
                break
            elif nbr==3:
                print(df3)
                break  
            elif nbr==4:
                print(df4)
                break
            elif nbr==5:
                print(df5)
                break
            elif nbr==6:
               
                print("You will now view Physics cycle.")
                physics()
            else:
                print("Wrong number!Try again.")
                nbr=1
                while nbr>7:
                   
                    nbr=1
                    nbr+=1 
            nbr+=1
                    
                   
                   
       
    else:
        print("Please try again")
        
        
        