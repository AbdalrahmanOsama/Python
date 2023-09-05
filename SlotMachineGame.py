import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

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


def get_slot_machine_spins(rows, cols, symbols):
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


#function collects input amount from the user
def deposit():
    while True:
        amount = input("Enter the deposit value: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a valid number.")
    return amount


#function gets the number of lines to bet on from the user
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines must be greater than zero and less than " + str(MAX_LINES) + ".")
        else:
            print("Please enter a valid number.")
    return lines


#function gets the amount of bet of each line
def get_bet():
    while True:
        bet = input(f"Enter the amount of bet on each line: ${MIN_BET}-${MAX_BET}. ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            elif MIN_BET > bet:
                print("Minimum amount of bet is $" + str(MIN_BET) + ".")
            elif bet > MAX_BET:
                print("Maximum amount of bet is $" + str(MAX_BET) + ".")
        else:
            print("Please enter a valid number.")
    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You cannot bet that amount, your current balance is ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines.\nTotal bet = ${total_bet}.")
    slots = get_slot_machine_spins(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won: {winnings}!!\nYou won on: {winning_lines}.")
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}.")
        spinning = input("Press ENTER to play or \"q\" to quit.")
        if spinning == "q":
            break
        else:
            balance += spin(balance)
    print(f"You left with ${balance}.")
    exit = input("Press any key to quit.")


main()
