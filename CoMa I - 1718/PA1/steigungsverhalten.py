def steigungsverhalten(a, b , c, d, x_0):
    erste_ableitung = 3 * a * x_0 * x_0 + 2 * b * x_0 + c
    if erste_ableitung > 0:
        print("An der Stelle " + str(x_0) + " steigt die Funktion.")
    elif erste_ableitung < 0:
        print("An der Stelle " + str(x_0) + " faellt die Funktion.")
    else:
        zweite_ableitung = 6 * a * x_0 + 2 * b
        if zweite_ableitung > 0:
            print("An der Stelle " + str(x_0) + " hat die Funktion ein lokales Minimum.")
        elif zweite_ableitung < 0:
            print("An der Stelle " + str(x_0) + " hat die Funktion ein lokales Maximum.")
        else:
            print("An der Stelle " + str(x_0) + " hat die Funktion einen kritischen Punkt unbekannten Typs.")
