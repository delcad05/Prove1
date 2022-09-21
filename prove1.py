# W01 Prove: Developer - Adam Del Castillo-Call


num = 1
playArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def render():
    line = ""
    i = 1
    while i != 10:
        if i == 9:
            line += f"{playArr[i-1]}"
            print(line)
            line = ""
        elif i%3 == 0:
            line += f"{playArr[i-1]}"
            print(line)
            print("--+---+--")
            line = ""
        else:           
            line += f"{playArr[i-1]}" + " | "

        i += 1

def userInput(turn):
    print()
    if turn % 2 == 0:
        change = int(input("o's turn to choose a square (1-9): "))
        if playArr[change-1] == "x" or playArr[change-1] == "o":
            while playArr[change-1] == "x" or playArr[change-1] == "o":
                print("That spot is already taken. Try again.")
                print()
                change = int(input("o's turn to choose a square (1-9): "))

            playArr[change-1] = "o"
        else:
            playArr[change-1] = "o"
    else:
        change = int(input("x's turn to choose a square (1-9): "))
        if playArr[change-1] == "x" or playArr[change-1] == "o":
            while playArr[change-1] == "x" or playArr[change-1] == "o":
                print("That spot is already taken. Try again.")
                print()
                change = int(input("o's turn to choose a square (1-9): "))

            playArr[change-1] = "x"
        else:
            playArr[change-1] = "x"
    print()
    
def checkWin():
    i = 0
    while i != 9:
        if i == 0:
            if playArr[i] == "x":
                if playArr[i+3] == "x":
                    if playArr[i+6] == "x":
                        return True, "x"
                elif playArr[i+4] == "x":
                    if playArr[i+8] == "x":
                        return True, "x"
                elif playArr[i+1] == "x":
                    if playArr[i+2] == "x":
                        return True, "x"
            if playArr[i] == "o":
                if playArr[i+3] == "o":
                    if playArr[i+6] == "o":
                        return True, "o"
                elif playArr[i+4] == "o":
                    if playArr[i+8] == "o":
                        return True, "o"
                elif playArr[i+1] == "o":
                    if playArr[i+2] == "o":
                        return True, "o"
        elif i == 1:
            if playArr[i] == "x":
                if playArr[i+3] == "x":
                    if playArr[i+6] == "x":
                        return True, "x"
            elif playArr[i] == "o":
                if playArr[i+3] == "o":
                    if playArr[i+6] == "o":
                        return True, "o"
        elif i == 2:
            if playArr[i] == "x":
                if playArr[i+3] == "x":
                    if playArr[i+6] == "x":
                        return True, "x"
                if playArr[i+2] == "x":
                    if playArr[i+4] == "x":
                        return True, "x"
            if playArr[i] == "o":
                if playArr[i+3] == "o":
                    if playArr[i+6] == "o":
                        return True, "o"
                if playArr[i+2] == "o":
                    if playArr[i+4] == "o":
                        return True, "o"
        elif i == 3:
            if playArr[i] == "x":
                if playArr[i+1] == "x":
                    if playArr[i+2] == "x":
                        return True, "x"
            elif playArr[i] == "o":
                if playArr[i+1] == "o":
                    if playArr[i+2] == "o":
                        return True, "o"
        elif i == 4:
            if playArr[i] == "x":
                if playArr[i+1] == "x":
                    if playArr[i+2] == "x":
                        return True, "x"
            elif playArr[i] == "o":
                if playArr[i+1] == "o":
                    if playArr[i+2] == "o":
                        return True, 'o'
        i += 1
    return False, "no one"

            


def main():
    i = 1
    turn = 1
    win = False
    while i != 9 and win == False:
        render()
        userInput(turn)
        win, winner = checkWin()
        i += 1
        turn += 1
    print()
    render()
    print()
    if win == True:
        print("Yay! A winner")
        print(f"Player {winner.capitalize()} Wins!")
    if win == False:
        print("Oh no, a draw")        
        print(f"{winner.capitalize()} wins")


main()