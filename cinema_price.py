film = input("Choose the film(Friday,Champions,Feathered gang):")
date = input("Choose the date(Today,Tommorow):")
time = int(input("Choose the time:"))
nticket = int(input("Write the number of tickets:"))
if film == "Friday":
    if date == "Today":
        if time == 12:
            if nticket < 20:
                print("Cost is", 250*nticket, "rubles")
            else:
                print("Cost is", 250*nticket*0.8, "rubles")
        elif time == 16:
            if nticket < 20:
                print("Cost is", 350*nticket, "rubles")
            else:
                print("Cost is", 350*nticket*0.8, "rubles")
        elif time == 20:
            if nticket < 20:
                print("Cost is", 450*nticket, "rubles")
            else:
                print("Cost is", 450*nticket*0.8, "rubles")
    else:
        if time == 12:
            if nticket < 20:
                print("Cost is", 250*nticket*0.95, "rubles")
            else:
                print("Cost is", 250*nticket*0.8*0.95, "rubles")
        elif time == 16:
            if nticket < 20:
                print("Cost is", 350*nticket*0.95, "rubles")
            else:
                print("Cost is", 350*nticket*0.8*0.95, "rubles")
        elif time == 20:
            if nticket < 20:
                print("Cost is", 450*nticket*0.95, "rubles")
            else:
                print("Cost is", 450*nticket*0.8*0.95, "rubles")
elif film == "Champions":
    if date == "Today":
        if time == 10:
            if nticket < 20:
                print("Cost is", 250*nticket, "rubles")
            else:
                print("Cost is", 250*nticket*0.8, "rubles")
        elif time == 13:
            if nticket < 20:
                print("Cost is", 350*nticket, "rubles")
            else:
                print("Cost is", 350*nticket*0.8, "rubles")
        elif time == 16:
            if nticket < 20:
                print("Cost is", 350*nticket, "rubles")
            else:
                print("Cost is", 350*nticket*0.8, "rubles")
    else:
        if time == 10:
            if nticket < 20:
                print("Cost is", 250*nticket*0.95, "rubles")
            else:
                print("Cost is", 250*nticket*0.8*0.95, "rubles")
        elif time == 13:
            if nticket < 20:
                print("Cost is", 350*nticket*0.95, "rubles")
            else:
                print("Cost is", 350*nticket*0.8*0.95, "rubles")
        elif time == 16:
            if nticket < 20:
                print("Cost is", 350*nticket*0.95, "rubles")
            else:
                print("Cost is", 350*nticket*0.8*0.95, "rubles")
elif film == "Feathered gang":
    if date == "Today":
        if time == 10:
            if nticket < 20:
                print("Cost is", 350*nticket, "rubles")
            else:
                print("Cost is", 350*nticket*0.8, "rubles")
        elif time == 14:
            if nticket < 20:
                print("Cost is", 450*nticket, "rubles")
            else:
                print("Cost is", 450*nticket*0.8, "rubles")
        elif time == 18:
            if nticket < 20:
                print("Cost is", 450*nticket, "rubles")
            else:
                print("Cost is", 450*nticket*0.8, "rubles")
    else:
         if time == 10:
            if nticket < 20:
                print("Cost is", 350*nticket*0.95, "rubles")
            else:
                print("Cost is", 350*nticket*0.8*0.95, "rubles")
         elif time == 14:
            if nticket < 20:
                print("Cost is", 450*nticket*0.95, "rubles")
            else:
                print("Cost is", 450*nticket*0.8*0.95, "rubles")
         elif time == 18:
            if nticket < 20:
                print("Cost is", 450*nticket*0.95, "rubles")
            else:
                print("Cost is", 450*nticket*0.8*0.95, "rubles")
