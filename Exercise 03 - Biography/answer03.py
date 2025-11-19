name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter your age as a number.")
bio = {
    "Name": name,
    "Hometown": hometown,
    "Age": age}
 
print(f"{bio['Name']}\n{bio['Hometown']}\n{bio['Age']}")
