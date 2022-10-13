def timeConverter(hours, minutes):
    if hours <0 or hours >24 or minutes <0 or minutes >59:
        return(print("This is not possible! Please enter a valid number"))
    if hours>12:
        hours = hours-12
        return(print("The time is " + str(hours) + ":" + str(minutes) + "pm"))
    else:
        return(print("The time is " + str(hours) + ":" + str(minutes) + "am"))

timeConverter(24, 59)