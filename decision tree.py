print("Welcome to the Golf Decision Tree!")
print("Answer the following questions to determine if you should play golf today.")

# Decision tree structure with numeric conditions
outlook = int(input("What is the outlook? (1=sunny, 2=overcast, 3=rainy): "))

if outlook == 1:
    humidity = int(input("What is the humidity? (1=high, 2=normal): "))
    if humidity == 1:
        print("Decision: No")
    elif humidity == 2:
        print("Decision: Yes")

elif outlook == 2:
    print("Decision: Yes")

elif outlook == 3:
    windy = int(input("Is it windy? (1=true, 2=false): "))
    if windy == 1:
        print("Decision: No")
    elif windy == 2:
        print("Decision: Yes")

else:
    print("Invalid input. Please enter 1 (sunny), 2 (overcast), or 3 (rainy).")
