def main():
  hydrogen = int(input("Please enter the number of Hydrogen molecules"))
  oxygen = int(input("Please enter the number of Oxygen molecules"))
  carbon = int(input("Please enter the number of Carbon molecules"))
  weight = (hydrogen * 1.00794) + (oxygen * 12.0107) + (carbon * 15.9994)
  print("The comnined molecular weight is ",weight)

main()
