if __name__ == '__main__':
    print("Welcome to the tip calculator.")
    total_bill = input("What was the total bill? ")
    tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
    people_count = input("How many people to split the bill? ")
    total_amount = (float(total_bill) / int(people_count)) * (1 + 0.01 * float(tip_percentage))
    print(f"Each person should pay : ${round(total_amount, 2)}")

  
