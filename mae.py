from sys import stdout

def get_part_of_day(hour):
    global time
    if 5 <= hour <= 11:
        time = "Morning"
    elif 12 <= hour <= 17:
        time = "Afternoon"
    elif 18 <= hour <= 22:
        time = "Evening"
    else:
        time = "error"
    return time

# If you want to use current hour:
# from datetime import datetime
# h = datetime.now().hour
# stdout.write('have a good {0}!\n'.format(get_part_of_day(h)))


for h in range(0, 24):
    stdout.write('hour {0} is {1}\n'.format(h, get_part_of_day(h)))