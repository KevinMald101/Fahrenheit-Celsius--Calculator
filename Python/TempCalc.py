def CCalculator(Fahrenheit):
    Celsius = (int(Fahrenheit) - 32) * .5556
    print(str(Celsius) + "°C")

def FCalculator(Celsius):
    Fahrenheit = (int(Celsius) * 1.8) + 32
    print(str(Fahrenheit) + "°F")

def inputAmount():
    #create sentinel loop asking for input and checking if it is number
    # if it is NOT number repeat
    Amount = input();
    while not Amount.isdigit():
        print("Your input: {} is not a number.".format(Amount))
        Amount = input()
    return Amount
    
isInputWrong = True
while isInputWrong:
    print("What would you like to calculate: Fahrenheit or Celsius")
    Type = input().lower()
    Inputs = ["fahrenheit", "f", "celsius", "c"]
    isInputWrong = False

    if Type == "fahrenheit" or "f":
        print("Amount you want to make Celsius:")
        Amount = inputAmount()
        CCalculator(Amount)
    elif Type == "celsius" or "c":
        print("Amount you want to make Fahrenheit:")
        Amount = inputAmount()
        FCalculator(Amount)
    else:
        isInputWrong = True
        print("Your input of {} was not a valid input type".format(Type))


