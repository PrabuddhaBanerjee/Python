def main():
  print("This program calculates the future value")
  print("Of a 10 year Investment")
  principal = eval(input("Input the amount of principal:"))
  apr = eval(input("Enter the rate of Interest"))
  for i in range(10):
    principal = principal * (1 + apr)
  print("The principal amount comes out to:", principal, " for 10 years")

main();
