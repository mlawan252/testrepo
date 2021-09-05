#Display the output
print("New python File")
# program that print out the factors of a given integer

number = int(input("Enter a positive integer  "))
for i in range(1,number + 1):
             if number % i == 0:
                 print(f"{i} is a factor of {number}")
