import time
marks1=int(input("Enter your 1st mark: "))
marks2=int(input("Enter your 2nd mark: "))
marks3=int(input("Enter your 3rd mark: "))

def total():
    total2=(marks1+marks2+marks3)
    return(total2)

def average():
    average2=(marks1+marks2+marks3)/3
    return(average2)

time.sleep(2)

print("Student Mark Report")
print("Total Marks-",total())
print("Average Marks-",average())

time.sleep(5)
