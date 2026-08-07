def main():
    greeting = greet(
        input("Greeting: ")
    )

def greet(to):
    to = to.strip().casefold()
    if to.startswith('h') == True:
        print("$0")
    else:
        print("$100")

main()    