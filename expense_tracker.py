#Name:Diya Kumal
#Date:09-10-2025
#Lab Title:Simple Expense Tracker
print("Welcome to the Simple Expense Tracker!")
print("This program helps you record and analyse your daily expenses. \n")

#Task 2: Input and Data collection
category=[]
amount=[]

while True:
   category= input("Enter expense category (e.g.,Food,Travel): ")
   amount= float(input("Enter amount: "))

   category.append(category)
   amount.append(amount)

   more = input("Do you want to add more? (yes/no): ").lower()
   if more != "yes":
       break
   
#Task 3:Expense calculations
total = sum(amount)
average = total / len(amount)

#Task 4: Neatly Formatted Output
print("\nYour Expenses:")
for i in range(len(category)):
   print(f"{category[i]} - {amount[i]}")

print("\nTotal Expense:", total)
print("Average Expense:", average)

#Bonus: Save to file
with open("expense.txt", "w") as file:
   file.write("Expenses Record\n")
   for i in range(len(category)):
      file.write(f"{category[i]} - {amount[i]}\n")
   file.write(f"Total Expense: {total}\n")
   file.write(f"Average Expense: {average}\n")

print("\nAll expenses saved in 'expense.txt'.")      

                 




    



    


