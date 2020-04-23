def main():
  print("This program is calculate sum of first n numbers")
  num = int(input("Please enter value for n"))
  sum = 0
  for i in range(1,num+1):
    sum += i
  print("Sum of n natural numbers is ", sum)

main()
