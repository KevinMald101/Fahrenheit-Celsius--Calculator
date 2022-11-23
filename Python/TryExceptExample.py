case = 0
try:
    if case ==0:
        float("3")
    elif case==1:
        float("3.a")
    elif case ==2:
        float([])
    elif case==3:
        "whoops" + 3
    elif case==3:
        "whoops" + 3
    elif case ==4:
        100/0
except ValueError:
    print("the input to float was wrong")
except TypeError:
    print("can't add string to a number")
except:
    print("I don't know what kind of error this is")

