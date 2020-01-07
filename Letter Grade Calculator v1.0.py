#Instructions:
#When we read code and predict its output, 
#it is called tracing code.

#For this lesson, you will come up with your own challenging 
#algorithm for other students to trace. 
#It must contain at least 5 if statements and 
#use at least one AND or OR boolean condition.

#For this challenge try reading 3 or 4 of your classmates' 
#code—trace the code and predict what it outputs, 
#then run it in the Sandbox to see if you got it right.


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
    
    
    
    