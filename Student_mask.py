student_mask = {'Pankaj' : 99, 'Ajay Sharma' : 88, 'Rohan Das' : 69,
                'Aman' : 34, 'Shivam' : 78, 'Abhisek Yadev' : 39 }
print("for Exit type 'q'")
while True:
    Selecting_stu = input("Enter the Student's name: ")
    if Selecting_stu == 'q':
        break
    try:
        find = student_mask[Selecting_stu]
        print(f"{Selecting_stu+"'s"} marks: {find}")

    except KeyError:
        print("Student not Found")







