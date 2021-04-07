# Creates a text file containing the final average for the current grading

def average_program():
    print("\nEnter Student's Full Name: \n")
    name = str(input())

    print("\nEnter Grade Level: \n")
    grade_level = int(input())

    print("\n!!!Follow the Prompt!!!")

    print("\nEnter Math Average: \n")
    math_input = float(input())

    print("\nEnter A.P Average: \n")
    ap_input = float(input())

    print("\nEnter Science Average")
    sci_input = float(input())

    print("\nEnter Filipino Average: \n")
    fil_input = float(input()) 

    print("\nEnter English Average: \n")
    eng_input = float(input())

    print("\nEnter Music Average: \n")
    music_input = float(input())

    print("\nEnter Art Average: \n")
    art_input = float(input())

    print("\nEnter P.E Average: \n")
    pe_input = float(input())

    print("\nEnter Health Average: \n")
    health_input = float(input())

    print("\nEnter Computer Average: \n")
    comp_input = float(input())

    print("\nEnter Ched Average: \n")
    ched_input = float(input())

    subject_add = (math_input + ap_input + sci_input + fil_input + eng_input + music_input + art_input + pe_input + health_input + comp_input + ched_input)
    final_average = (subject_add / 11)
    print("\nAverage Grade = \n" + str(final_average))
    print("\n Done!\n")

    write_grade = open(r"C:\Users\Amazing\Documents\Notepad files\Average Grade.txt", "a")

    write_grade.write("\nName: ")
    write_grade.write(str(name))
    write_grade.write("\nGrade Level: ")
    write_grade.write(str(grade_level))
    write_grade.write("\nAverage Grade: ")
    write_grade.write(str(final_average))
    write_grade.write("\n")

    write_grade.close()

average_program()
