def main():
    print("This program")
    x = eval(input("Enter num between 0 and 1:"))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print( x )
main()
