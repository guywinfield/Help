# Poloniex Strategy

coins = 0
quantity = 0


def bitcoin(question1,question):
    response = input(question1)
    divide = float(response)
    response = input(question)
    bitcoin = float(response)
    tier_bitcoin = bitcoin / divide
    print("You should use",tier_bitcoin, " per coin you invest in\n")
    return tier_bitcoin

def quantity(question):
    response = input(question)
    coins = float(response)
    coins = coins / 5
    print("You should use", coins," per tier of sell order\n")
    return coins

def pricing(question):
    response = input(question)
    price = float(response)
    pricex2 = price * 2
    print("1st tier price: ",pricex2)
    pricex3 = price * 3
    print("2nd tier price: ",pricex3)
    pricex4 = price * 4
    print("3rd tier price: ",pricex4)
    pricex6 = price * 6
    print("4th tier price: ",pricex6)
    pricex10 = price * 10
    print("5th tier price: ",pricex10)
    return pricex2, pricex3, pricex4, pricex6, pricex10

def main():
    print("""   This is the Poloniex Strategy Program, Please follow thr instructions
                                Press Q to exit the program
""")
    bitcoin("How many coins would you like to invest in? ","How much Bitcoin do you have? ")
    exit = None
    while exit != "Q":
        quantity("How many coins do you possess? ")
        pricing("What is the current value of your coin? ")
        exit = input("\nPress the ENTER key to start again or Q to exit: ")

main()
input("\nEnter any Key to exit program")

            
