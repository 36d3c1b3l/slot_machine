import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3





def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter a number greater than 0.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"How much lines would you like to bet on (1-{MAX_LINES} lines)? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a number between 1 and 3.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        bet = input(f"How much would you like to bet ({MIN_BET}-{MAX_BET})? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a number between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet



def render(columns):
    n = len(columns[0])
    m = len(columns)
    for i in range(n):
        for j in range(m):
            if j == m - 1:
                print(f"{columns[j][i]}", end="\n")
            else: 
                print(f"{columns[j][i]}", end=" | ")


def spin_machine(rows, cols, symbols):
    symbols_available = []

    for char, count in symbols.items():
        for _ in range(count):
            symbols_available.append(char)

    columns = []
    for i in range(cols):
        column = []
        sym_copy = symbols_available[:]
        #print(f"Col{i}:\n")
        for j in range(rows):
            value = random.choice(sym_copy)
            sym_copy.remove(value)
            column.append(value)
            #print(f"{column[j]} ", end="")
        #print("\n")
        columns.append(column)
    return columns


def get_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            if symbol != col[line]:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings, winning_lines


def game(balance):
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"Not enough money: balance: {balance}; total bet: {total_bet}")
        else:
            break
    print(f"Your total bet on {lines} lines is {total_bet}$")

    symbol_count = {
    "A": 3,
    "B": 4,
    "C": 5,
    "D": 6
    }

    symbol_weight = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
    }
    
    spin = spin_machine(ROWS, COLS, symbol_count)
    print("Your spin:")
    render(spin)
    winnings, wlines = get_winnings(spin, lines, bet, symbol_weight)
    print(f"You won ${winnings}.\n You won on lines:", *wlines)
    return winnings - total_bet

def main():
    balance = deposit()
    while balance > 0:
        print(f"Current balance is ${balance}")
        spin = input("Press enter/q to spin/quit")
        if spin == "q":
            break;
        balance += game(balance)
    print(f"You left with {balance}")
    



if __name__ == "__main__":
    main()