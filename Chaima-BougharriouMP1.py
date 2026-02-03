import random # Importing random module for the spending challenge
# Function to start the expense tracker
def start_expense_tracker():
    print('Welcome to Personal Expense Treacker !')
#giving the name of user(x is the name)
    x=input("Please enter your name:")
    print(f"Hello,{x}!Let's start tracking your espenses!")
# spending and goal variable  
    total_spending = 0.0
    total_goal = 0.0
# expenses of category
    expenses = {"Food": 0.0, "Transport": 0.0, "Entertainment": 0.0}
# infinitif loop for the menu
    while True:
# display the main menu
        print("1. Add an expense")
        print("2. Check spending threshold")
        print("3. Set a savings goal")
        print("4. Check savings goal progress")
        print("5. View spending report")
        print("6. Challenge")
        print("7. Reset tracker")
        print("8. Exit")
        choice=int(input("enter your choice(1-8):"))

# **Option 1: Add an expense**
            
        if choice==1:
                amount=float(input("Enter expense amount:"))# get expense amount
                Categories = {1: 'Food', 2: 'Transport', 3: 'Entertainment'}# match category numbers to names
                print("Categories: 1. Food, 2. Transport, 3. Entertainment")
                category_choice = int(input("Enter category number (1-3): "))# get category name
                if category_choice==1 or category_choice==2 or category_choice==3 :
                    category = Categories[category_choice]
                    expenses[category] += amount# to know how much we should add to the food
                    total_spending += amount # Update total spending
                    print(f"Expense of {amount} added for {category}!")
                    print(f"Your total spending so far is: {total_spending}\n")
                else:
                    print("Invalid category choice. Please try again.")
# **Option 2: 

        elif choice==2:
                limit=float(input("Enter your spending limit:"))
                total_limit=limit+.0
                if total_spending<total_limit:
                    print(f'Good news{x}!Your total {total_spending} is below your limit {total_limit}\n')
                else:
                    print(f'Good news{x}!Your total {total_spending} is below your limit {total_limit}\n')
# **Option 3: 
        elif choice==3:
                goal=float(input("Enter your weekly  savings goal:"))
                total_goal=goal+.0
                print(f'Savings goal set to {total_goal},keep tracking your goal {x}!')
# **Option 4
        elif choice == 4:
                amount=float(input("Enter expense amount:"))
                goal=float(input("Enter your weekly  savings goal:"))
                total_spending += amount
                total_goal=goal+.0
                
                difference = total_goal - total_spending  # Use existing values, don't ask for new inputs
                print(f"Your savings goal is {total_goal} and total spent {total_spending}.")  # Removed extra period

                if difference > 0:
                    print(f"You’re on track, {x}! You can still save {difference} this week.")  # Proper spacing
                elif difference < 0:
                    print(f"Watch out your spending, {x}! You’ve overspent by {abs(difference)}.")  # Proper formatting
                else:
                    print(f"No savings, {x}!")  # Proper sentence structure
 # **Option 5              
        elif choice==5:
#display the submenu:
             while True: 
                print("\nSpending Report Menu:")
                print("1. View detailed spending by category")
                print("2. View total spending")
                print("3. Back to main menu")

                sub_choice = int(input("Enter your choice (1-3): "))

                if sub_choice == 1:
                    print(f"\nSpending Report for {x}:")
                    print(f"Food: {expenses['Food']}")
                    print(f"Transport: {expenses['Transport']}")
                    print(f"Entertainment: {expenses['Entertainment']}")
                    print(f"Total Spending: {total_spending}")

                elif sub_choice == 2:
                    print(f"\nTotal Spending: {total_spending}")
                    # Show total spending 
                elif sub_choice == 3:
                    print("Returning to the main menu...")
                    break  # Return to the main menu

                else:
                    print("Invalid choice, try again.")
# **Option 6:
        elif choice==6:
               #  selects a spending category randomly
                challenge_category = random.choice(["Food", "Transport", "Entertainment"])
                print("Random Category Challenge:")
                print(f"This week, focus on reducing your spending in: {challenge_category}!")
                print(f"Try to cut back on {challenge_category} expenses and save more. You’ve got this, {x}!")
# **Option 7:                
        elif choice==7:
                confirm=input("Are you sure you want to reset all totals? (yes/no):")
                if confirm=="yes":
                    total_spending = 0.0# Reset total spending
                    expenses = {"Food": 0.0, "Transport": 0.0, "Entertainment": 0.0}# Reset category spending
                    print(f'Tracker reset successfully,{x}!')
                else:
                    print("canceled!")
# **Option 8:
        while True:
                
                if choice == 8:
                    print(f"Done with tracking your expenses! Stay financially smart, {x}!")
                    break  # Exits the loop when choice is 8

                # **Treat invalid menu choices**
                elif choice < 1 or choice > 8:
                    print("Invalid choice! Please enter a number between 1 and 8.")
                    break


start_expense_tracker()            
                    

                    
                    
                
                    
                
                            


                
                
                
    
    