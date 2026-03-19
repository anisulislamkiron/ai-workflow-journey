def main ():
    user_input = input ("What time is it? ")
    converted_time = convert(user_input)
    if 7<= converted_time <=8:
        print("Breakfast Time")
    elif 2<= converted_time <=3:
        print("Lunch Time")
    if 17<= converted_time <=18:
        print("Dinner Time")

def convert (time):
    hour, minutes = time.split(":")
    hour = float(hour)
    minutes = float(minutes)/60
    return hour + minutes

if __name__=="__main__":
    main()
