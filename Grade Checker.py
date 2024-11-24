# Title of programme
print ("THIS PROGRAMME CALCULATES YOUR GPA AND CGPA")

# Collects user name
fullname=str(input("ENTER YOUR FULLNAME HERE:"))

# Collects the number of semesters in integers only
while True:
    try:
        no_of_semesters=int(input("HOW MANY SEMESTER(s) DO YOU INTEND CHECKING CGPA FOR?: "))
        break
    except:
        print("That is not a number!")

# Function that calculates credit unit and quality point
def maincalc():
    total_grade_list=[]
    total_credit_unit=[]

    # Collects number of courses in integer only
    while True:
        try:
            no_of_courses=int(input("HOW MANY COURSES IN SEMESTER "+str(number+1)+": "))
            break
        except:
            print("That is not a number!")   

    # Iterate through the number of courses
    for x in range(int(no_of_courses)):
        # Collects credit unit in integer only
        while True:
            try:
                credit_unit=int(input("HOW MANY CREDIT UNIT IN COURSE "+str(x+1)+" OF SEMESTER "+str(number+1)+": "))
                break
            except:
                print("That is not a number!")     
        # Conditional statement to categorize grades
        grade=str(input("INPUT GRADE: "))          
        if (grade.lower()=="a"):
            y=5
        elif (grade.lower()=="b"):
            y=4
        elif (grade.lower()=="c"):
            y=3
        elif (grade.lower()=="d"):
            y=2
        elif (grade.lower()=="e"):
            y=1
        else:
            y=0
        # Appending grades and credit unit to a list
        total_grade_list.append(y)
        total_credit_unit.append(credit_unit)
    sum_total_credit_unit=sum(total_credit_unit)
    product=[]
    # Iterating through grades list and total credit unit list and multiplying them accordingly and then appending result to another list
    for num1,num2 in zip(total_grade_list,total_credit_unit):
        product.append(num1*num2)
    # Final calculation for the semester and display of GPA
    sum_product=sum(product)
    total=float(sum_product/sum_total_credit_unit)
    gpa=(round(total, 2))
    print("YOUR GPA FOR THIS SEMESTER IS: "+str(gpa))
    print("***************************************")
    return sum_product, sum_total_credit_unit

# List to append quality point and sum of credit unit to
list1=[]
list2=[]

# Iterating through the number of semesters
for number in range(int(no_of_semesters)):
    sum_product, sum_total_credit_unit = maincalc()
    list1.append(sum_product)
    list2.append(sum_total_credit_unit)
# Final calculation for CGPA across all indicated semesters
total = sum(list1)/sum(list2)
cgpa1 = round(total, 2)
print(str(fullname.upper())+", YOUR TOTAL CGPA IS: "+str(cgpa1))
print("******************************************")