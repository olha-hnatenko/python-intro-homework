while True:
  try:
      number = float(input("Enter a number: "))
      print(number)
      break
  except ValueError:
      print("That's not a valid number. Try again.")