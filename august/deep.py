def main ():
    answer = ans (input("What is the Great Question of Life, the Universe and Everything? "))
     
    
def ans (to):
    to = to.strip().casefold()
    if to == "42":
        print ("Yes")
    elif to == "forty-two":
        print ("Yes")
    elif to == "forty two":
        print ("Yes")
    else:
        print ("No ")

main ()