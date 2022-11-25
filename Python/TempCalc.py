def CCalculator(Fahrenheit):
    Celsius = (int(Fahrenheit) - 32) /1.8
    print(str(Celsius) + "°C")

def FCalculator(Celsius):
    Fahrenheit = (int(Celsius) * 1.8) + 32
    if Fahrenheit <= freezingPointF:
        print("Freezing point reached")
    if Fahrenheit >= boilingPointF:
        print("Boiling point reached")
    
    print(str(Fahrenheit) + "°F")

def inputAmount():
    #create sentinel loop asking for input and checking if it is number
    # if it is NOT number repeat
    Amount = input();
    while not Amount.isdigit():
        print("Your input: {} is not a number.".format(Amount))
        Amount = input()
    return Amount
    
freezingPointC = 0
freezingPointF = 32
boilingPointF = 212
isInputWrong = True
while isInputWrong:
    #print("What unit would you like to use: Fahrenheit or Celsius")
    Type = input("What unit would you like to use: Fahrenheit or Celsius: ").lower()
    isInputWrong = False

    if Type == 'fahrenheit' or Type == 'f':
        print("Amount you want to make Celsius:")
        Amount = inputAmount()
        CCalculator(Amount)
    elif Type == 'celsius' or Type == 'c':
        print("Amount you want to make Fahrenheit:")
        Amount = inputAmount()
        FCalculator(Amount)
    else:
        isInputWrong = True
        print("Your input of \" {} \" was not a valid input type".format(Type))


