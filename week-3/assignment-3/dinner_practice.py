time = int(input("How much time do you have to cook? Enter minutes: "))
chicken = input("Do you have chicken at home? (yes/no): ").lower()

if time < 15:
    print("You can make an omelette.")
elif time >= 15 and chicken == "yes":
    print("Great! You can make chicken with vegetables.")
elif time >= 15 and chicken == "no":
    print("Sounds good! You can make pasta.")
else:
    print("Please answer yes or no.")