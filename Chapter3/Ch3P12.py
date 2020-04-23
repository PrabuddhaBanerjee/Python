def main():
  print("This program is calculate sum of cube of first n numbers")
  num = int(input("Please enter value for n"))
  sum = 0
  for i in range(1,num+1):
    sum += (i ** 3)
  print("Sum of cubes of n natural numbers is ", sum)

main()
