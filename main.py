try:
  print("Enter a number between 1 and 10:")
  number = int(input())
except ValueError:
  print("You must enter a number between 1 and 10:")
  number = int(input())
  if number >= 1 and number <= 10 :
    not_validated = False
  else:
    print("Number entered out of range")
    print("Enter a number between 1 and 10:")
    number = int(input())