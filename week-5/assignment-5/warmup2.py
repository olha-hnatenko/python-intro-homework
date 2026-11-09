answer = input("Enter a positive integer: ")
while not answer.isdigit() or int(answer)<=0:
    print("That's not a positive integer. Try again.")
    answer = input("Enter a positive integer: ")
print(f"Got it: {answer}")