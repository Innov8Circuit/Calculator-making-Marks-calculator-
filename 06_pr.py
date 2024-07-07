# Input marks
a1 = int(input("Enter your marks of English: "))
a2 = int(input("Enter your marks of Hindi: "))
a3 = int(input("Enter your marks of Math: "))
a4 = int(input("Enter your marks of Science: "))
a5 = int(input("Enter your marks of S.St: "))
a6 = int(input("Enter your marks of Computer: "))

# Check if all marks are within valid range
if any(mark < 0 or mark > 100 for mark in [a1, a2, a3, a4, a5, a6]):
    print("Invalid marks entered! Please enter marks between 0 and 100.")
else:
    # Calculate percentage
    total_marks = a1 + a2 + a3 + a4 + a5 + a6
    percentage = (total_marks / 600) * 100

    # Determine grade
    if percentage >= 90:
        grade = "Excellent"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Print result
    print(f"Your grade is: {grade}")
    print(f"Your percentage is: {percentage:.2f}%")


input("Press Enter to close the program...")