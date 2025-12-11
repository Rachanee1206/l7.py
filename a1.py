med=input("Do you have medical cause for absentees:")
att= int(input("Enter your attendance in number:"))
if med=="yes" or med=="Yes" or med=="YES":
    print("You are allowed to sit in exam")
else:
    if att>=75:
        print("You are allowed to sit in exam")
    else:
        print("You are not allowed to sit in exam ") 
        
