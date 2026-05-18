courses = ["Python", "Data Structures", "Maths"]
registrations = []
rr="✅ Registration Successfully Completed!"


# Step 1: Show courses with numbers
print("Available Courses:")
for i in range(len(courses)):
    print(f"{i+1}. {courses[i]}")

# Step 2: Input
regno =input("\nEnter your registration no:")
name = input("Enter your name: ")
choice = int(input("Select course number: "))

# Step 3: Validate choice
if choice < 1 or choice > len(courses):
    print("Invalid course selection!")
else:
    selected_course = courses[choice - 1]
    registrations.append((name, selected_course))

    # Step 4: Show registration
    print("\n--- Your Registration Details ---")
    print("Registration No :",regno)
    print("Student Name :", name)
    print("Course       :", selected_course)

    # Step 5: Modify option
    while True:
        print("\nDo you want to modify your registration?")
        print("1. Yes")
        print("2. No (Complete Registration)")

        option = input("Enter choice: ")

        if option == "1":
            print("\nAvailable Courses:")
            for i in range(len(courses)):
                print(f"{i+1}. {courses[i]}")

            new_choice = int(input("Select new course number: "))

            if 1 <= new_choice <= len(courses):
                selected_course = courses[new_choice - 1]
                registrations[0] = (regno,name, selected_course)

                print("\n--- Updated Registration ---")
                print("Registration No;", regno)
                print("Student Name :", name)
                print("Course       :", selected_course)
            else:
                print("Invalid selection!")

        elif option == "2":
            print(rr.center(50,'-'))
            print("Final Details:")
            print("Regtration No:",regno)
            print("Student Name :", name)
            print("Course       :", selected_course)


            break

        else:
            print("Invalid choice!")