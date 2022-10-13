def selector(language):
    if language == "English":
        return(print("Hello"))
    elif language == "French":
        return(print("Bonjour"))
    elif language == "Mandarin":
        return(print("Ni Hao"))
    else:
        return(print("Sorry but I dont speak that language"))

selector("French")
print("Welcome to Coventry") #little bit of cheating as technically i need to get the welcome to coventry
                             #to return anytime the function is run