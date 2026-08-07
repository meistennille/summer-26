#This is a program that tells the user the meal time of the day!!

def main():
    time = input("What time is it? ")
    meal = convert (time)
    print (meal)

def convert(time):
    hours, minutes = time.split(":", maxsplit=1)
    mins, meridian = minutes.split(" ")
    if meridian == "pm" and int(hours) < 12:
        hours = int(hours) + 12 
    current_time = float (hours + int(mins) / 60)
    if 8.0 >= current_time >= 7.0:
        return "breakfast time"
    elif 13.0 > current_time >= 12.0:
        return "lunch time"
    elif 19.0 > current_time >= 18.0:
        return "dinner time"

if __name__ == "__main__":
    main()