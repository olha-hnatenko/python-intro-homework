while True:
  try:
      numerator = float(input("Enter the numerator: "))
      denominator = float(input('Enter the denominator: '))
      print(f"{numerator} ÷ {denominator} = {numerator/denominator}")
      break
  except ZeroDivisionError:
      print("Can't divide by zero — please try a non-zero denominator.\n")