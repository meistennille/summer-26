#to determine if a number is even or odd
def main():
    a = int(input("What is a? "))
    if parity(a):
        print ("a is even.")
    else:
        print("a is odd.")

def parity(n):
    return n % 2 == 0 

main() 
    