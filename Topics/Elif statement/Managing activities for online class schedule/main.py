# The program starts here

def activity(day):
    #Use elif to set conditions for days of the week
    # Remember, the days are represented as follows:
    # 0 to 4 for Monday to Friday respectively
    # 5 for Saturday
    # 6 for Sunday

    # Write your code here!

    weekday = day
    if 0 >= weekday <= 4:
        return "Study!"
    elif weekday == 5:
        return "Rest!"
    elif weekday == 6:
        return "Leisure!"


# Do not change anything below!

day = int(input())
print(activity(day))