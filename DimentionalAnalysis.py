BaseUnits = ["Meters", "Seconds", "Grams", "Liters"]
Prefixes = ["Giga", "Mega", "Kilo", "Deci", "Centi", "Milli", "Micro", "Nano", "Pico"]
print('''Welcome to Jackson's Unit Conversion Program!
    Meters = 1
    Seconds = 2
    Grams = 3
    Liters = 4
      ''')
base=input("Please enter the number of the base unit you would like to convert FROM:")
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
pre = input("Please enter the number of the prefix you would like to convert FROM:")
amt = input("Please enter the amount you would like to convert:")
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
convert = input("Please enter the number of the prefix you would like to convert TO:")

if pre == '1' and base == '1' and convert == '2':
    print(f"{amt} GigaMeters is equal to {amt*1000} MegaMeters")