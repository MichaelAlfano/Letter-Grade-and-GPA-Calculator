#Number grade to Letter grade solver
numbergrade = int(input("Enter your number grade:"))

if (numbergrade >= 0 and numbergrade < 60):
    print("Your letter grade: F")
    
elif (numbergrade >= 60 and numbergrade < 63):
    print("Your letter grade: D-")
elif (numbergrade >= 63 and numbergrade < 67):
    print("Your letter grade: D")
elif (numbergrade >= 67 and numbergrade < 80):
    print("Your letter grade: D+")
    
elif (numbergrade >= 70 and numbergrade < 73):
    print("Your letter grade: C-")
elif (numbergrade >= 73 and numbergrade < 77):
    print("Your letter grade: C")
elif (numbergrade >= 77 and numbergrade < 80):
    print("Your letter grade: C+")
    
elif (numbergrade >= 80 and numbergrade < 83):
    print("Your letter grade: B-")
elif (numbergrade >= 83 and numbergrade < 87):
    print("Your letter grade: B")
elif (numbergrade >= 87 and numbergrade < 90):
    print("Your letter grade: B+")
    
elif (numbergrade >= 90 and numbergrade < 93):
    print("Your letter grade: A-")
elif (numbergrade >= 93 and numbergrade < 97):
    print("Your letter grade: A")
elif (numbergrade >= 97 and numbergrade < 100):
    print("Your letter grade: A=")
    
else:
    print("Number grade is invalid")
    
    
    
    
