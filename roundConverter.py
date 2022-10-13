def timeConverter(hours, minutes):
    if hours <0 or hours >24 or minutes <0 or minutes >59:
        return(print("This is not possible! Please enter a valid number"))
    if hours>12 and minutes>30:
        hours = hours-12
        if minutes<8:
            minutes = "00"
        elif minutes<23:
            minutes = 15
        elif minutes<38:
            minutes = 30
        elif minutes<52:
            minutes = 45
        else:
            minutes = "00"
            hours = hours+1
        
        return(print("The time is about #" + str(hours) + ":" + str(minutes) + "pm"))

    else:
        if minutes<8:
            minutes = "00"
        elif minutes<23:
            minutes = 15
        elif minutes<38:
            minutes = 30
        elif minutes<52:
            minutes = 45
        else:
            minutes = "00"
            hours = hours+1
        return(print("The time is about " + str(hours) + ":" + str(minutes) + "am"))

timeConverter(13, 53)