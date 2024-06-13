#https://www.youtube.com/watch?v=th4OBktqK1I&t=2448s
import random

#all caps hedder global constant
#i python er den en constant der ikke vil ældre værdi
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def deposit():
    #run while is true
    while True:
        amount = input("What would you like to deposit? $")
        #check if input is an digit
        if amount.isdigit():
            #convert to an int
            amount = int(amount)
            #check if amount is greater than 0
            if amount > 0:
                #break cus all is true
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    #run while is true
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        #check if input is an digit
        if lines.isdigit():
            #convert to an int
            lines = int(lines)
            #check if amount is greater than 0
            if 1 <= lines <= MAX_LINES:
                #break cus all is true
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    #run while is true
    while True:
        amount = input("What would you like to bet on each line? $")
        #check if input is an digit
        if amount.isdigit():
            #convert to an int
            amount = int(amount)
            #check if amount is greater than 0
            if MIN_BET <= amount <= MAX_BET:
                #break cus all is true
                break
            else:
                #with f"" we can put variables in a between "" like so with {}
                #The variables will automaticly be converted to string
                print(f"Bet must be between {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    # check if they have a large enough balance to the amount they wish to bet
    while True:
        bet = get_bet()
        total_bet = bet * lines
        # is total_bet larger than their balance
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"you won on", *winning_lines)
    return winnings - total_bet
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == 'q':
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
main()
