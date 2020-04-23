def main():
  print("This program calculates the future value")
  print("Of a 10 year Investment")
  principal = eval(input("Input the amount of principal:"))
  apr = eval(input("Enter the rate of Interest: "))
  time = eval(input("Enter the number of years: "))
  simple_interest = (principal * apr * time) / 100
  print("The Simple Interest comes out to:", simple_interest)

main();
