def main():
  print("This program is calculate sum of first n numbers by user input")
  num = int(input("How many numbers you want to sum "))
  sum = 0
  for i in range(1,num+1):
    sum += int(input("Please enter the number"))
  print("Sum of", num ,"numbers is ", sum)

main()
