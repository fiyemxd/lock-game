def main():
    valid_represent = False
    while valid_represent == False:
        try:    
            p1_represent = input("Enter a character to represent player 1: ").upper()
            while (len(p1_represent) != 1) or p1_represent == " ":
                p1_represent = input("Enter a character to represent player 1: ").upper()
            p2_represent = input("Enter a character to represent player 2: ").upper()
            while (len(p2_represent) != 1) or p2_represent == " " or p2_represent == p1_represent:
                p2_represent = input("Enter a character to represent player 2: ").upper()
        except:
            print("Invalid entry.")
        else:
            valid_represent = True

    valid_side_length = False
    while valid_side_length == False:        
        try:    
            side_length=int(input('Enter the row/column number of the playing field(4-8): '))
            while (side_length < 4) or (side_length > 8):
                side_length=int(input('Enter the row/column number of the playing field(4-8): '))
        except ValueError:
            print("Invalid entry.")
        else:
            valid_side_length = True

    coordinates = [[' ' for i in range(side_length)] for j in range(side_length)]  # create a coordinate list based on side length
    for a in range(side_length): # fill for the initial state of the field
        coordinates[0][a]=p2_represent
        coordinates[-1][a]=p1_represent
    play_counter=0
    p1_counter = side_length
    p2_counter = side_length # number of stones

    new_board(coordinates,side_length,play_counter, p1_represent, p2_represent, p1_counter, p2_counter)

def new_board(coordinates,side_length,play_counter, p1_represent, p2_represent, p1_counter, p2_counter):
    horizontal=['A','B','C','D','E','F','G','H']
    vertical=[1,2,3,4,5,6,7,8]
    for row in range(side_length):
        if row == 0:
            for col in range(side_length):
                if col == 0:
                    print('    ',horizontal[col], end='  ')
                else:
                    print('  ',horizontal[col], end='  ')
            print()
            for boundary in range(side_length):
                if boundary == 0:
                    print('  -------', end='')
                else:
                    print('------', end='')

        print()
        for col in range(side_length):
            if col == 0:
                print(vertical[row], '| ', coordinates[row][col], end='  |  ')
            else:
                print(coordinates[row][col], end='  |  ')
            if col==side_length-1:
                print(vertical[row])

        for boundary in range(side_length):
            if boundary == 0:
                print('  -------', end='')
            else:
                print('------', end='')
        
    print()
    for hor in range(side_length):
        if hor == 0:
            for col in range(side_length):
                if col == 0:
                    print('    ',horizontal[col], end='  ')
                else:
                    print('  ',horizontal[col], end='  ')
                

        places={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
        print()

        if (p1_counter < 2): # game end check
            print("Player 2 wins!")
            ans = play_again()
            if ans in "nN":
                return False
            elif ans in "yY":
                main()
        elif (p2_counter < 2):
            print("Player 1 wins!")
            ans = play_again()
            if ans in "nN":
                return False
            elif ans in "yY":
                main()

    play(coordinates,side_length,places,play_counter, p1_represent, p2_represent, p1_counter, p2_counter)
def play(coordinates,side_length,places,play_counter, p1_represent, p2_represent, p1_counter, p2_counter):
    places_inverted = {"0":"A", "1":"B", "2":"C", "3":"D", "4":"E", "5":"F", "6":"G", "7": "H"} # it only serves to print which stone has been removed
    if play_counter%2==1:
        print("player 2's turn ")
        whose_turn = p2_represent
        move_x, move_y, stone_x, stone_y = assign_location(places) # get the position input  
        movement_rules(coordinates, places,play_counter, p1_represent, p2_represent, move_x, move_y, stone_x, stone_y) # check the movement rules    
    elif play_counter%2==0:
        print("player 1's turn ")
        whose_turn = p1_represent
        move_x, move_y, stone_x, stone_y = assign_location(places)   
        movement_rules(coordinates, places,play_counter, p1_represent, p2_represent, move_x, move_y, stone_x, stone_y)     
    
    # locked stone check
    for k in range(side_length):
        for m in range(side_length-2): # to avoid indexerror
            if coordinates[k][m] == p1_represent: 
                if coordinates[k][m+1]==p2_represent and coordinates[k][m+2]==p1_represent: # p2 horizontal
                    if whose_turn!=p2_represent: # to restrain suicide
                        coordinates[k][m+1] = ' '
                        print(f"The stone at position {k+1}{places_inverted[str(m+1)]} was locked and removed.")
                        p2_counter -= 1
            elif coordinates[k][m] == p2_represent :
                if coordinates[k][m+1]==p1_represent and coordinates[k][m+2]==p2_represent: # p1 horizontal
                    if whose_turn!=p1_represent: 
                        coordinates[k][m+1] = ' '
                        print(f"The stone at position {k+1}{places_inverted[str(m+1)]} was locked and removed.")
                        p1_counter -= 1
    for i in range(side_length-2): # to avoid indexerror
        for j in range(side_length):
            if coordinates[i][j] == p1_represent:    
                if coordinates[i+1][j]==p2_represent and coordinates[i+2][j]==p1_represent: # p2 vertical
                    if whose_turn!=p2_represent:
                        coordinates[i+1][j] = ' '
                        print(f"The stone at position {i+2}{places_inverted[str(j)]} was locked and removed.")
                        p2_counter -= 1
            elif coordinates[i][j] == p2_represent:
                if coordinates[i+1][j]==p1_represent and coordinates[i+2][j]==p2_represent: # p1 vertical
                    if whose_turn!=p1_represent:
                        coordinates[i+1][j] = ' '
                        print(f"The stone at position {i+2}{places_inverted[str(j)]} was locked and removed.")
                        p1_counter -= 1

    if (coordinates[0][side_length-1]==p1_represent): # top right corner p1
        if coordinates[1][side_length-1]==p2_represent and coordinates[0][side_length-2]==p2_represent:
            coordinates[0][side_length-1]=' '
            print(f"The stone at position 1{places_inverted[str(side_length-1)]} was locked and removed.")
            p1_counter -= 1
    elif (coordinates[0][side_length-1]==p2_represent): # top right corner p2
        if coordinates[1][side_length-1]==p1_represent and coordinates[0][side_length-2]==p1_represent:
            coordinates[0][side_length-1]=' '
            print(f"The stone at position 1{places_inverted[str(side_length-1)]} was locked and removed.")
            p2_counter -= 1

    if coordinates[0][0]==p1_represent: # top left corner p1
        if coordinates[0][1]==p2_represent and coordinates[1][0]==p2_represent:
            coordinates[0][0]=' '
            print(f"The stone at position 1A was locked and removed.")
            p1_counter -= 1
    elif coordinates[0][0]==p2_represent: # top left corner p2
        if coordinates[0][1]==p1_represent and coordinates[1][0]==p1_represent:
            coordinates[0][0]=' '
            print(f"The stone at position 1A was locked and removed.")
            p2_counter -= 1

    if coordinates[side_length-1][0]==p1_represent: # bottom left corner p1
        if coordinates[side_length-2][0]==p2_represent and coordinates[side_length-1][1]==p2_represent:
            coordinates[side_length-1][0]=' '
            print(f"The stone at position {side_length}A was locked and removed.")
            p1_counter -= 1
    elif coordinates[side_length-1][0]==p2_represent: # bottom left corner p2
        if coordinates[side_length-2][0]==p1_represent and coordinates[side_length-1][1]==p1_represent:
            coordinates[side_length-1][0]=' '
            print(f"The stone at position {side_length}A was locked and removed.")
            p2_counter -= 1

    if coordinates[side_length-1][side_length-1]==p1_represent: # bottom right corner p1
        if coordinates[side_length-1][side_length-2]==p2_represent and coordinates[side_length-2][side_length-1]==p2_represent:
            coordinates[side_length-1][side_length-1]=' '
            print(f"The stone at position {side_length}{places_inverted[str(side_length-1)]} was locked and removed.")
            p1_counter -= 1
    elif coordinates[side_length-1][side_length-1]==p2_represent: # bottom right corner p2
        if coordinates[side_length-1][side_length-2]==p1_represent and coordinates[side_length-2][side_length-1]==p1_represent:
            coordinates[side_length-1][side_length-1]=' '
            print(f"The stone at position {side_length}{places_inverted[str(side_length-1)]} was locked and removed.")
            p2_counter -= 1

    play_counter+=1 # to determine whose turn
    new_board(coordinates,side_length,play_counter, p1_represent, p2_represent, p1_counter, p2_counter)
    
def play_again():
    valid_yes_no = False
    while valid_yes_no == False:    
        try:
            yes_no = input("Do you want to play again(yYnN): ")
            while (yes_no not in "yYnN"):
                yes_no = input("Do you want to play again(yYnN): ")
        except:
            print("Invalid entry.")
        else:
            return yes_no

def movement_rules(coordinates, places,play_counter, p1_represent, p2_represent, move_x, move_y, stone_x, stone_y):
    if play_counter%2==1:
        whose_turn = p2_represent
    elif play_counter%2==0:
        whose_turn = p1_represent    
    try:
        while coordinates[stone_y][stone_x]!=whose_turn or coordinates[move_y][move_x]!=' ': # valid stone control
            print('Invalid entry. ')
            move_x, move_y, stone_x, stone_y = assign_location(places)   
        
        
        while (stone_y != move_y) and (stone_x != move_x): # straight move control
            print('stones have to move straight,please enter again. ')
            move_x, move_y, stone_x, stone_y = assign_location(places)   

    except:
        print("Invalid entry.")
        move_x, move_y, stone_x, stone_y = assign_location(places) # if any exception occurs get positions again

    if (move_x - stone_x > 0):
        for hor_control_right in range(1,move_x-stone_x): # check if there is a stone on right
            if coordinates[stone_x+hor_control_right][stone_y] == p1_represent or coordinates[stone_x+hor_control_right][stone_y] == p2_represent:
                print("You can't jump over any stone.")
                move_x, move_y, stone_x, stone_y = assign_location(places)
                movement_rules(coordinates, places,play_counter, p1_represent, p2_represent, move_x, move_y, stone_x, stone_y)   
                return False

    elif (move_x - stone_x < 0):
        for hor_control_left in range(1,stone_x-move_x): # check if there is a stone on left
            if coordinates[stone_x-hor_control_left][stone_y] == p1_represent or coordinates[stone_x-hor_control_left][stone_y] == p2_represent:
                print("You can't jump over any stone.")
                move_x, move_y, stone_x, stone_y = assign_location(places)   
                movement_rules(coordinates, places,play_counter, p1_represent, p2_represent, move_x, move_y, stone_x, stone_y) 
                return False

    if (move_y - stone_y > 0):
        for vert_control_up in range(1,move_y - stone_y): # check if there is a stone upwards
            if coordinates[stone_y+vert_control_up][stone_x] == p1_represent or coordinates[stone_y+vert_control_up][stone_x] == p2_represent:
                print("You can't jump over any stone.")
                move_x, move_y, stone_x, stone_y = assign_location(places)   
                movement_rules(coordinates, places,play_counter, p1_represent, p2_represent, move_x, move_y, stone_x, stone_y)
                return False

    elif (move_y - stone_y < 0):
        for vert_control_down in range(1,stone_y - move_y): # check if there is a stone beneath
            if coordinates[stone_y-vert_control_down][stone_x]  == p1_represent or coordinates[stone_y-vert_control_down][stone_x]  == p2_represent:
                print("You can't jump over any stone.")
                move_x, move_y, stone_x, stone_y = assign_location(places)   
                movement_rules(coordinates, places,play_counter, p1_represent, p2_represent, move_x, move_y, stone_x, stone_y)  
                return False
      

    
    coordinates[stone_y][stone_x]=' '
    coordinates[move_y][move_x]=whose_turn # assign the stone


def assign_location(places):
    valid_positions = False
    while valid_positions == False:    
        try:
            positions = input("please enter the position of your own stone you want to move and the target position: ") 
            print("-------------------------------------------------------------------------------------")
            stone = positions.split()[0]
            move=positions.split()[1]
            while stone == move:
                positions = input("please enter the position of your own stone you want to move and the target position: ") 
                stone = positions.split()[0]
                move=positions.split()[1]
    
            stone_y, stone_x =int(stone[0])-1,places[stone[1].upper()] # assigning coordinates to current position
            move_y, move_x =int(move[0])-1,places[move[1].upper()] # assigning coordinates to target position
        except:
            print("Invalid value.")
        else:
            valid_positions = True
    return move_x, move_y, stone_x, stone_y

main()
