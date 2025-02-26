BaseUnits = ["Meters", "Time", "Grams", "Liters"]
Prefixes = ["Giga", "Mega", "Kilo", "Deci", "Centi", "Milli", "Micro", "Nano", "Pico"]
ConversionFactors = {
    "Giga": 1e9,
    "Mega": 1e6,
    "Kilo": 1e3,
    "Deci": 1e-1,
    "Centi": 1e-2,
    "Milli": 1e-3,
    "Micro": 1e-6,
    "Nano": 1e-9,
    "Pico": 1e-12
}
TimeConversionFactors = {
    "Seconds": 1,
    "Minutes": 60,
    "Hours": 3600,
    "Days": 86400,
    "Weeks": 604800,
    "Months": 2628000,
    "Years": 31536000
}
TimeBaseUnits = ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"]
print('''Welcome to Jackson's Unit Conversion Program!''')
while True:
    print('''   
        Meters = 1
        Time = 2
        Grams = 3
        Liters = 4
        ''')

    base=int(input("Please enter the number of the base unit you would like to convert FROM:")) -1
    BaseIndex = BaseUnits[base]  
    if base == 1:
        print('''Great! Which incriment of time would you like to convert FROM:
        Seconds = 1
        Minutes = 2
        Hours = 3
        Days = 4
        Weeks = 5
        Months = 6
        Years = 7
        ''')
        Tpre = int(input("Please enter the number of the increment of time you would like to convert FROM:")) -1
        TimeIndex = TimeBaseUnits[Tpre]
        TimeAmt = int(input("Please enter the amount you would like to convert:"))
        print('''Great! Which incriment of time would you like to convert TO:
        Seconds = 1
        Minutes = 2
        Hours = 3
        Days = 4
        Weeks = 5
        Months = 6
        Years = 7
        ''')
        Tconvert = int(input("Please enter the number of the increment of time you would like to convert TO:")) -1
        TimeConvertIndex = TimeBaseUnits[Tconvert]

        TimeConvertPre = TimeConversionFactors[TimeIndex]
        TimeConvertPost = TimeConversionFactors[TimeConvertIndex]
        print(f"{TimeAmt} {TimeIndex} is equal to {TimeAmt*TimeConvertPre/TimeConvertPost} {TimeConvertIndex}")

    else:
        print('''Great! Now lets choose the prefix you would like to convert FROM:  
          Giga = 1 
          Mega = 2 
          Kilo = 3  
          Deci = 4  
          Centi = 5  
          Milli = 6  
          Micro = 7  
          Nano = 8  
          Pico = 9     
            ''')
        pre= int(input("Please enter the number of the prefix you would like to convert FROM:")) -1
        PreIndex = Prefixes[pre]  
        amt = int(input("Please enter the amount you would like to convert:")) 
        print('''Great! Now lets choose the prefix you would like to convert TO:  
          Giga = 1  
          Mega = 2  
          Kilo = 3  
          Deci = 4  
          Centi = 5  
          Milli = 6  
          Micro = 7  
          Nano = 8  
          Pico = 9  
            ''')

        convert = int(input("Please enter the number of the prefix you would like to convert TO:")) -1
        ConvertIndex = Prefixes[convert]

        convertPre = ConversionFactors[PreIndex]
        convertPost = ConversionFactors[ConvertIndex]
        print(f"{amt} {PreIndex}{BaseIndex} is equal to {amt*convertPre/convertPost} {ConvertIndex}{BaseIndex}")


    cont = input("Would you like to convert another value? (yes or no)")
    if cont == "no":
        print("Thank you for using Jackson's Unit Conversion Program!")
        break
    else:
        continue


