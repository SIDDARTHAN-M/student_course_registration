FILE_NAME = "data.txt"

print("\n====== ADMIN PANEL ======")

while True:
    print("\n1. View All Students")
    print("2. Search by Registration No")
    print("3. Exit")

    choice = input("Enter choice: ")

    
    if choice == "1":
        print("\n--- Registered Students ---")

        try:
            with open(FILE_NAME, "r") as file:
                found = False

                for line in file:
                    data = line.strip().split(",")

                    print("Registration No :", data[0])
                    print("Student Name    :", data[1])
                    print("Course          :", data[2])
                    print("-----------------------------")

                    found = True

                if not found:
                    print("No records found!")

        except FileNotFoundError:
            print("No data file found!")

   
    elif choice == "2":
        regno = input("Enter Registration No: ")

        try:
            with open(FILE_NAME, "r") as file:
                found = False

                for line in file:
                    data = line.strip().split(",")

                    if data[0] == regno:
                        print("\n--- Student Found ---")
                        print("Registration No :", data[0])
                        print("Student Name    :", data[1])
                        print("Course          :", data[2])
                        found = True
                        break

                if not found:
                    print("Student not found!")

        except FileNotFoundError:
            print("No data file found!")

 
    elif choice == "3":
        print("Exiting Admin Panel...")
        break

    else:
        print("Invalid choice!")