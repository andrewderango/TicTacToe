from tkinter import *
import random
from math import inf as infinity
import time

root = Tk()
root.resizable(False, False)
root.geometry("675x650")
root.title('TicTacToe')
root.configure(background="#151326")

winning_possibilities = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
current_board_pieces = {1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None}

def placed_x_1():
    global x_image_1
    global x_label_1

    x_image_1 = PhotoImage(file="Images/x_barlow.png")
    x_label_1 = Label(root, image=x_image_1, bg="#151326")
    x_label_1.pack()
    x_label_1.place(x=204, y=117, anchor=CENTER)

    blank_button_1.place_forget()

    current_board_pieces[1] = 'x'
    check_win_user(True, True)

def placed_x_2():
    global x_image_2
    global x_label_2

    x_image_2 = PhotoImage(file="Images/x_barlow.png")
    x_label_2 = Label(root, image=x_image_2, bg="#151326")
    x_label_2.pack()
    x_label_2.place(x=337.5, y=117, anchor=CENTER)

    blank_button_2.place_forget()

    current_board_pieces[2] = 'x'
    check_win_user(True, True)

def placed_x_3():
    global x_image_3
    global x_label_3

    x_image_3 = PhotoImage(file="Images/x_barlow.png")
    x_label_3 = Label(root, image=x_image_3, bg="#151326")
    x_label_3.pack()
    x_label_3.place(x=471, y=117, anchor=CENTER)

    blank_button_3.place_forget()
    
    current_board_pieces[3] = 'x'
    check_win_user(True, True)

def placed_x_4():
    global x_image_4
    global x_label_4

    x_image_4 = PhotoImage(file="Images/x_barlow.png")
    x_label_4 = Label(root, image=x_image_4, bg="#151326")
    x_label_4.pack()
    x_label_4.place(x=204, y=250, anchor=CENTER)

    blank_button_4.place_forget()

    current_board_pieces[4] = 'x'
    check_win_user(True, True)

def placed_x_5():
    global x_image_5
    global x_label_5

    x_image_5 = PhotoImage(file="Images/x_barlow.png")
    x_label_5 = Label(root, image=x_image_5, bg="#151326")
    x_label_5.pack()
    x_label_5.place(x=337.5, y=250, anchor=CENTER)

    blank_button_5.place_forget()

    current_board_pieces[5] = 'x'
    check_win_user(True, True)

def placed_x_6():
    global x_image_6
    global x_label_6

    x_image_6 = PhotoImage(file="Images/x_barlow.png")
    x_label_6 = Label(root, image=x_image_6, bg="#151326")
    x_label_6.pack()
    x_label_6.place(x=471, y=250, anchor=CENTER)

    blank_button_6.place_forget()

    current_board_pieces[6] = 'x'
    check_win_user(True, True)

def placed_x_7():
    global x_image_7
    global x_label_7

    x_image_7 = PhotoImage(file="Images/x_barlow.png")
    x_label_7 = Label(root, image=x_image_7, bg="#151326")
    x_label_7.pack()
    x_label_7.place(x=204, y=383, anchor=CENTER)

    blank_button_7.place_forget()

    current_board_pieces[7] = 'x'
    check_win_user(True, True)

def placed_x_8():
    global x_image_8
    global x_label_8

    x_image_8 = PhotoImage(file="Images/x_barlow.png")
    x_label_8 = Label(root, image=x_image_8, bg="#151326")
    x_label_8.pack()
    x_label_8.place(x=337.5, y=383, anchor=CENTER)

    blank_button_8.place_forget()

    current_board_pieces[8] = 'x'
    check_win_user(True, True)

def placed_x_9():
    global x_image_9
    global x_label_9

    x_image_9 = PhotoImage(file="Images/x_barlow.png")
    x_label_9 = Label(root, image=x_image_9, bg="#151326")
    x_label_9.pack()
    x_label_9.place(x=471, y=383, anchor=CENTER)

    blank_button_9.place_forget()

    current_board_pieces[9] = 'x'
    check_win_user(True, True)

def check_win_user(score_adj, next_turn):
    global wins
    global losses
    global ties

    win_exists = False
    for winning_possibility_ticker in winning_possibilities:
        if current_board_pieces[winning_possibility_ticker[0]] == 'x' and current_board_pieces[winning_possibility_ticker[1]] == 'x' and current_board_pieces[winning_possibility_ticker[2]] == 'x':
            win_exists = True
    if win_exists == True:
        if score_adj == True:
            print('X wins!')
            wins += 1
            # print(wins, losses, ties)
        record_label.configure(text=(str(wins) + ' - ' + str(losses) + ' - ' + str(ties)))
        forfeit_button.configure(image=clear_image)

        blank_button_1["state"] = "disabled"
        blank_button_2["state"] = "disabled"
        blank_button_3["state"] = "disabled"
        blank_button_4["state"] = "disabled"
        blank_button_5["state"] = "disabled"
        blank_button_6["state"] = "disabled"
        blank_button_7["state"] = "disabled"
        blank_button_8["state"] = "disabled"
        blank_button_9["state"] = "disabled"
        return True
    else:
        if next_turn == True:
            # print('CPUs turn now. X does not win.')
            cpu_turn()
        else:
            return False

def check_win_cpu(score_adj):
    win_exists = False
    for winning_possibility_ticker in winning_possibilities:
        if current_board_pieces[winning_possibility_ticker[0]] == 'o' and current_board_pieces[winning_possibility_ticker[1]] == 'o' and current_board_pieces[winning_possibility_ticker[2]] == 'o':
            win_exists = True
    if win_exists == True:
        global losses
        global wins
        global ties
        if score_adj == True:
            print('O wins!')
            losses += 1
            # print(wins, losses, ties)
        record_label.configure(text=(str(wins) + ' - ' + str(losses) + ' - ' + str(ties)))
        forfeit_button.configure(image=clear_image)
        return True
    else:
        # if score_adj == True:
            # print('Humans turn now. CPU does not win.')
        return False

def check_win(hypothetical_board_pieces):
    for winning_possibility_ticker in winning_possibilities:
        if hypothetical_board_pieces[winning_possibility_ticker[0]] == 'x' and hypothetical_board_pieces[winning_possibility_ticker[1]] == 'x' and hypothetical_board_pieces[winning_possibility_ticker[2]] == 'x':
            return -1
        elif hypothetical_board_pieces[winning_possibility_ticker[0]] == 'o' and hypothetical_board_pieces[winning_possibility_ticker[1]] == 'o' and hypothetical_board_pieces[winning_possibility_ticker[2]] == 'o':
            return 1

    none_finder_list = []
    for item in hypothetical_board_pieces:
        none_finder_list.append(hypothetical_board_pieces[item])
    if None not in none_finder_list:
        return 0

    return None

def find_available_moves(state):
    available_moves = []
    for board_spots in state:
        if current_board_pieces[board_spots] == None:
            available_moves.append(board_spots)

    return available_moves
    
def minimax(state, depth, player):
    global next_minimax_player, simulations

    simulations += 1
    best_moves_list = []

    if depth == 0 or check_win(state) == 1 or check_win(state) == -1 or check_win(state) == 0:
        # print('Result: ' + str(check_win(state)))
        score = {'Position': None, 'Score': check_win(state)}
        return score

    if player == 'o':
        best = {'Position': None, 'Score': -2}
    else:
        best = {'Position': None, 'Score': 2}

    for availableMove in find_available_moves(state):
        # print(find_available_moves(state))
        state[availableMove] = player
        # print(state)

        if player == 'o':
            next_minimax_player = 'x'
        elif player == 'x':
            next_minimax_player = 'o'

        score = minimax(state, depth - 1, next_minimax_player)
        score['Position'] = availableMove
        state[availableMove] = None
        # print(state)

        if depth == 9:
            if score['Score'] > best['Score']:
                best_moves_list.clear()
                best_moves_list.append(score)
            elif score['Score'] == best['Score']:
                best_moves_list.append(score)

        if player == 'o':
            if score['Score'] > best['Score']:
                best = score
        else:
            if score['Score'] < best['Score']:
                best = score

        # print('Score: ' + str(score))
        # print('Best: ' + str(best))
        # print('Player: ' + str(player))
        # print('Depth: ' + str(depth))
        # print('\n')

    # print('Returned best: ' + str(best))
    if depth == 9:
        print(best_moves_list)
        return random.choice(best_moves_list)
    else:
        return best

def cpu_turn():
    global difficulty
    global simulations

    simulations = 0

    blank_button_1["state"] = "disabled"
    blank_button_2["state"] = "disabled"
    blank_button_3["state"] = "disabled"
    blank_button_4["state"] = "disabled"
    blank_button_5["state"] = "disabled"
    blank_button_6["state"] = "disabled"
    blank_button_7["state"] = "disabled"
    blank_button_8["state"] = "disabled"
    blank_button_9["state"] = "disabled"

    if difficulty == 'Impossible':
        none_finder_list = []
        for item in current_board_pieces:
            none_finder_list.append(current_board_pieces[item])
        depth = len(none_finder_list)
        # print(minimax(current_board_pieces, depth, 'o'))

        cpu_execution(minimax(current_board_pieces, depth, 'o')['Position'], False)
        print('Results from ' + str(simulations) + ' simulations.')

    elif difficulty == 'Hard':
        # finding if cpu can win
        for a in current_board_pieces:
            if current_board_pieces[a] == None:
                current_board_pieces[a] = 'o'
                win_exists = False
                # print(current_board_pieces)
                for winning_possibility_ticker in winning_possibilities:
                    # print(winning_possibility_ticker)
                    if current_board_pieces[winning_possibility_ticker[0]] == 'o' and current_board_pieces[winning_possibility_ticker[1]] == 'o' and current_board_pieces[winning_possibility_ticker[2]] == 'o':
                        win_exists = True
                        # print('True!')
                if win_exists == True:
                    # print(str(a) + ' is a CPU win.')
                    cpu_execution(int(a), True)
                    return None
                # else:
                    # print(str(a) + ' is not a CPU win.')
                current_board_pieces[a] = None
                # print('\n')

        # finding if user can win
        for b in current_board_pieces:
            if current_board_pieces[b] == None:
                current_board_pieces[b] = 'x'
                win_exists = False
                # print(current_board_pieces)
                for winning_possibility_ticker in winning_possibilities:
                    # print(winning_possibility_ticker)
                    if current_board_pieces[winning_possibility_ticker[0]] == 'x' and current_board_pieces[winning_possibility_ticker[1]] == 'x' and current_board_pieces[winning_possibility_ticker[2]] == 'x':
                        win_exists = True
                        # print('True!')
                if win_exists == True:
                    # print(str(b) + ' is a human win.')
                    cpu_execution(int(b), False)
                    return None
                # else:
                    # print(str(b) + ' is not a human win.')
                current_board_pieces[b] = None
                # print('\n')

        # check if corners are open
        corner_availability = []
        for c in [1,3,7,9]:
            if current_board_pieces[c] == None:
                corner_availability.append(c)
        if len(corner_availability) > 0:
            cpu_execution(random.choice(corner_availability), False)
            return None

        # check if centre is open
        if current_board_pieces[5] == None:
            cpu_execution(5, False)
            return None

        # check if edges are open
        edge_availability = []
        for d in [2,4,6,8]:
            if current_board_pieces[d] == None:
                edge_availability.append(d)
        if len(edge_availability) > 0:
            cpu_execution(random.choice(edge_availability), False)
            return None

        # no possible cpu moves. Tie game. 
        cpu_execution(None, False)

    elif difficulty == 'Medium':
        # finding if cpu can win
        for a in current_board_pieces:
            if current_board_pieces[a] == None:
                current_board_pieces[a] = 'o'
                win_exists = False
                # print(current_board_pieces)
                for winning_possibility_ticker in winning_possibilities:
                    # print(winning_possibility_ticker)
                    if current_board_pieces[winning_possibility_ticker[0]] == 'o' and current_board_pieces[winning_possibility_ticker[1]] == 'o' and current_board_pieces[winning_possibility_ticker[2]] == 'o':
                        win_exists = True
                        # print('True!')
                if win_exists == True:
                    # print(str(a) + ' is a CPU win.')
                    cpu_execution(int(a), True)
                    return None
                # else:
                    # print(str(a) + ' is not a CPU win.')
                current_board_pieces[a] = None
                # print('\n')

        # finding if user can win
        for b in current_board_pieces:
            if current_board_pieces[b] == None:
                current_board_pieces[b] = 'x'
                win_exists = False
                # print(current_board_pieces)
                for winning_possibility_ticker in winning_possibilities:
                    # print(winning_possibility_ticker)
                    if current_board_pieces[winning_possibility_ticker[0]] == 'x' and current_board_pieces[winning_possibility_ticker[1]] == 'x' and current_board_pieces[winning_possibility_ticker[2]] == 'x':
                        win_exists = True
                        # print('True!')
                if win_exists == True:
                    # print(str(b) + ' is a human win.')
                    cpu_execution(int(b), False)
                    return None
                # else:
                    # print(str(b) + ' is not a human win.')
                current_board_pieces[b] = None
                # print('\n')
                # check if edges are open

        # pick random open square
        move_availability = []
        for d in current_board_pieces:
            if current_board_pieces[d] == None:
                move_availability.append(d)
        if len(move_availability) > 0:
            cpu_execution(random.choice(move_availability), False)
            return None

        cpu_execution(None, False)

    elif difficulty == 'Easy':
        # pick random open square
        move_availability = []
        for d in current_board_pieces:
            if current_board_pieces[d] == None:
                move_availability.append(d)
        if len(move_availability) > 0:
            cpu_execution(random.choice(move_availability), False)
            return None

        cpu_execution(None, False)

        

def cpu_execution(spot, cpu_win):
    global o_image_1
    global o_image_2
    global o_image_3
    global o_image_4
    global o_image_5
    global o_image_6
    global o_image_7
    global o_image_8
    global o_image_9

    global o_label_1
    global o_label_2
    global o_label_3
    global o_label_4
    global o_label_5
    global o_label_6
    global o_label_7
    global o_label_8
    global o_label_9

    if spot == None:
        global ties

        print('Tie game!')
        ties += 1
        # print(wins, losses, ties)
        record_label.configure(text=(str(wins) + ' - ' + str(losses) + ' - ' + str(ties)))
        forfeit_button.configure(image=clear_image)

    print('O is placed on ' + str(spot))

    if spot == 1:
        o_image_1 = PhotoImage(file="Images/o_barlow.png")
        o_label_1 = Label(root, image=o_image_1, bg="#151326")
        o_label_1.pack()
        o_label_1.place(x=204, y=117, anchor=CENTER)
        blank_button_1.place_forget()
        current_board_pieces[1] = 'o'
    elif spot == 2:
        o_image_2 = PhotoImage(file="Images/o_barlow.png")
        o_label_2 = Label(root, image=o_image_2, bg="#151326")
        o_label_2.pack()
        o_label_2.place(x=337.5, y=117, anchor=CENTER)
        blank_button_2.place_forget()
        current_board_pieces[2] = 'o'
    elif spot == 3:
        o_image_3 = PhotoImage(file="Images/o_barlow.png")
        o_label_3 = Label(root, image=o_image_3, bg="#151326")
        o_label_3.pack()
        o_label_3.place(x=471, y=117, anchor=CENTER)
        blank_button_3.place_forget()
        current_board_pieces[3] = 'o'
    elif spot == 4:
        o_image_4 = PhotoImage(file="Images/o_barlow.png")
        o_label_4 = Label(root, image=o_image_4, bg="#151326")
        o_label_4.pack()
        o_label_4.place(x=204, y=250, anchor=CENTER)
        blank_button_4.place_forget()
        current_board_pieces[4] = 'o'
    elif spot == 5:
        o_image_5 = PhotoImage(file="Images/o_barlow.png")
        o_label_5 = Label(root, image=o_image_5, bg="#151326")
        o_label_5.pack()
        o_label_5.place(x=337.5, y=250, anchor=CENTER)
        blank_button_5.place_forget()
        current_board_pieces[5] = 'o'
    elif spot == 6:
        o_image_6 = PhotoImage(file="Images/o_barlow.png")
        o_label_6 = Label(root, image=o_image_6, bg="#151326")
        o_label_6.pack()
        o_label_6.place(x=471, y=250, anchor=CENTER)
        blank_button_6.place_forget()
        current_board_pieces[6] = 'o'
    elif spot == 7:
        o_image_7 = PhotoImage(file="Images/o_barlow.png")
        o_label_7 = Label(root, image=o_image_7, bg="#151326")
        o_label_7.pack()
        o_label_7.place(x=204, y=383, anchor=CENTER)
        blank_button_7.place_forget()
        current_board_pieces[7] = 'o'
    elif spot == 8:
        o_image_8 = PhotoImage(file="Images/o_barlow.png")
        o_label_8 = Label(root, image=o_image_8, bg="#151326")
        o_label_8.pack()
        o_label_8.place(x=337.5, y=383, anchor=CENTER)
        blank_button_8.place_forget()
        current_board_pieces[8] = 'o'
    elif spot == 9:
        o_image_9 = PhotoImage(file="Images/o_barlow.png")
        o_label_9 = Label(root, image=o_image_9, bg="#151326")
        o_label_9.pack()
        o_label_9.place(x=471, y=383, anchor=CENTER)
        blank_button_9.place_forget()
        current_board_pieces[9] = 'o'

    if cpu_win == False:
        if check_win_cpu(True) == True:
            blank_button_1["state"] = "disable"
            blank_button_2["state"] = "disable"
            blank_button_3["state"] = "disable"
            blank_button_4["state"] = "disable"
            blank_button_5["state"] = "disable"
            blank_button_6["state"] = "disable"
            blank_button_7["state"] = "disable"
            blank_button_8["state"] = "disable"
            blank_button_9["state"] = "disable"
        elif check_win_cpu(True) == False:
            blank_button_1["state"] = "active"
            blank_button_2["state"] = "active"
            blank_button_3["state"] = "active"
            blank_button_4["state"] = "active"
            blank_button_5["state"] = "active"
            blank_button_6["state"] = "active"
            blank_button_7["state"] = "active"
            blank_button_8["state"] = "active"
            blank_button_9["state"] = "active"
        else:
            print('This should not happen')

    none_finder_list = []
    for item in current_board_pieces:
        none_finder_list.append(current_board_pieces[item])
    if None not in none_finder_list and none_finder_list.count('o') > none_finder_list.count('x'):
        ties += 1
        # print(current_board_pieces)
        record_label.configure(text=(str(wins) + ' - ' + str(losses) + ' - ' + str(ties)))

    # print(current_board_pieces)

    none_finder_list = []
    for item in current_board_pieces:
        none_finder_list.append(current_board_pieces[item])
    if None not in none_finder_list:
        forfeit_button.configure(image=clear_image)

def difficulty_change(difficulty_cmd):
    global difficulty
    global easy_active_image
    global easy_active_label
    global medium_active_image
    global medium_active_label
    global hard_active_image
    global hard_active_label
    global impossible_active_image
    global impossible_active_label

    print('Difficulty has been changed to ' + str(difficulty_cmd))
    difficulty = difficulty_cmd

    if difficulty_cmd == 'Easy':
        easy_active_image = PhotoImage(file="Images/easy_active.png")
        easy_active_label = Label(root, image=easy_active_image, bg="#151326")
        easy_active_label.pack()
        easy_active_label.place(x=127.5, y=500, anchor=CENTER)
        
        try:
            medium_active_label.place(x=1000, y=0)
        except:
            pass
        try:
            hard_active_label.place(x=1000, y=0)
        except:
            pass
        try:
            impossible_active_label.place(x=1000, y=0)
        except:
            pass

    elif difficulty_cmd == 'Medium':
        medium_active_image = PhotoImage(file="Images/medium_active.png")
        medium_active_label = Label(root, image=medium_active_image, bg="#151326")
        medium_active_label.pack()
        medium_active_label.place(x=267.5, y=500, anchor=CENTER)
        
        try:
            easy_active_label.place(x=1000, y=0)
        except:
            pass
        try:
            hard_active_label.place(x=1000, y=0)
        except:
            pass
        try:
            impossible_active_label.place(x=1000, y=0)
        except:
            pass

    elif difficulty_cmd == 'Hard':
        hard_active_image = PhotoImage(file="Images/hard_active.png")
        hard_active_label = Label(root, image=hard_active_image, bg="#151326")
        hard_active_label.pack()
        hard_active_label.place(x=407.5, y=500, anchor=CENTER)
        
        try:
            easy_active_label.place(x=1000, y=0)
        except:
            pass
        try:
            medium_active_label.place(x=1000, y=0)
        except:
            pass
        try:
            impossible_active_label.place(x=1000, y=0)
        except:
            pass

    elif difficulty_cmd == 'Impossible':
        impossible_active_image = PhotoImage(file="Images/impossible_active.png")
        impossible_active_label = Label(root, image=impossible_active_image, bg="#151326")
        impossible_active_label.pack()
        impossible_active_label.place(x=547.5, y=500, anchor=CENTER)
        
        try:
            easy_active_label.place(x=1000, y=0)
        except:
            pass
        try:
            medium_active_label.place(x=1000, y=0)
        except:
            pass
        try:
            hard_active_label.place(x=1000, y=0)
        except:
            pass

def forfeit_game():
    global x_label_1
    global x_label_2
    global x_label_3
    global x_label_4
    global x_label_5
    global x_label_6
    global x_label_7
    global x_label_8
    global x_label_9
    global o_label_1
    global o_label_2
    global o_label_3
    global o_label_4
    global o_label_5
    global o_label_6
    global o_label_7
    global o_label_8
    global o_label_9
    global current_board_pieces
    global ties

    try:
        x_label_1.place_forget()
    except:
        pass
    try:
        x_label_2.place_forget()
    except:
        pass
    try:
        x_label_3.place_forget()
    except:
        pass
    try:
        x_label_4.place_forget()
    except:
        pass
    try:
        x_label_5.place_forget()
    except:
        pass
    try:
        x_label_6.place_forget()
    except:
        pass
    try:
        x_label_7.place_forget()
    except:
        pass
    try:
        x_label_8.place_forget()
    except:
        pass
    try:
        x_label_9.place_forget()
    except:
        pass
    try:
        o_label_1.place_forget()
    except:
        pass
    try:
        o_label_2.place_forget()
    except:
        pass
    try:
        o_label_3.place_forget()
    except:
        pass
    try:
        o_label_4.place_forget()
    except:
        pass
    try:
        o_label_5.place_forget()
    except:
        pass
    try:
        o_label_6.place_forget()
    except:
        pass
    try:
        o_label_7.place_forget()
    except:
        pass
    try:
        o_label_8.place_forget()
    except:
        pass
    try:
        o_label_9.place_forget()
    except:
        pass

    none_finder_list = []
    for item in current_board_pieces:
        none_finder_list.append(current_board_pieces[item])

    if check_win_user(False, False) == False and check_win_cpu(False) == False and None in none_finder_list:
        global losses
        losses += 1
        record_label.configure(text=(str(wins) + ' - ' + str(losses) + ' - ' + str(ties)))

    forfeit_button.configure(image=forfeit_image)

    current_board_pieces = {1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None}

    blank_button_1.place(x=204, y=117, anchor=CENTER)
    blank_button_2.place(x=337.5, y=117, anchor=CENTER)
    blank_button_3.place(x=471, y=117, anchor=CENTER)
    blank_button_4.place(x=204, y=250, anchor=CENTER)
    blank_button_5.place(x=337.5, y=250, anchor=CENTER)
    blank_button_6.place(x=471, y=250, anchor=CENTER)
    blank_button_7.place(x=204, y=383, anchor=CENTER)
    blank_button_8.place(x=337.5, y=383, anchor=CENTER)
    blank_button_9.place(x=471, y=383, anchor=CENTER)

    blank_button_1["state"] = "active"
    blank_button_2["state"] = "active"
    blank_button_3["state"] = "active"
    blank_button_4["state"] = "active"
    blank_button_5["state"] = "active"
    blank_button_6["state"] = "active"
    blank_button_7["state"] = "active"
    blank_button_8["state"] = "active"
    blank_button_9["state"] = "active"

    if first_move == 'o' and current_board_pieces == {1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None}:
        cpu_execution(random.randint(1,9), False)

def toggle_first_move():
    global first_move

    if first_move == 'x':
        first_move = 'o'
        toggle_move_button.configure(image=o_first_move_image)
    elif first_move == 'o':
        first_move = 'x'
        toggle_move_button.configure(image=x_first_move_image)
    else:
        print('This should not happen.')

    if current_board_pieces == {1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None}:
        cpu_execution(random.randint(1,9), False)

def clear():
    submit_choices_button.place_forget()
    impossible_button_front.place_forget()
    easy_button_front.place_forget()
    med_button_front.place_forget()
    hard_button_front.place_forget()
    select_difficulty_label.place_forget()
    select_first_move_label.place_forget()
    o_first_move_label_front.place_forget()
    x_first_move_label_front.place_forget()
    ttt_title.place_forget()
    try:
        easy_active_label.place_forget()
    except:
        pass
    try:
        medium_active_label.place_forget()
    except:
        pass
    try:
        hard_active_label.place_forget()
    except:
        pass
    try:
        impossible_active_label.place_forget()
    except:
        pass
    try:
        x_first_move_label_active.place_forget()
    except:
        pass
    try:
        o_first_move_label_active.place_forget()
    except:
        pass

y_pos_slider=0

def slide():
    global y_pos_slider, slide_func_counter

    if y_pos_slider <= 650:
        y_pos_slider += 10
    else:
        cover_label.place_forget()
        return None

    if y_pos_slider == 500:
        if difficulty == 'Easy':
            easy_active_label.place(x=127.5, y=500, anchor=CENTER)
        elif difficulty == 'Medium':
            medium_active_label.place(x=267.5, y=500, anchor=CENTER)
        elif difficulty == 'Hard':
            hard_active_label.place(x=407.5, y=500, anchor=CENTER)
        elif difficulty == 'Impossible':
            impossible_active_label.place(x=547.5, y=500, anchor=CENTER)

    cover_label.place(y=y_pos_slider)
    root.after(10, slide)

    if slide_func_counter == 65:
        time.sleep(1)
        check_fm()
    slide_func_counter += 1

def change_fm(new_fm):
    global first_move, x_first_move_image_active, o_first_move_image_active, o_first_move_image_active, o_first_move_label_active, x_first_move_label_active
    print('First move has been changed to ' + str(new_fm))
    first_move = new_fm

    if new_fm == 'x':
        x_first_move_image_active = PhotoImage(file="Images/x_first_move_active.png")
        x_first_move_label_active = Label(root, image=x_first_move_image_active, bg="#151326")
        x_first_move_label_active.pack()
        x_first_move_label_active.place(x=207.5, y=300, anchor=CENTER)
        
        try:
            o_first_move_label_active.place(x=1000, y=0)
        except:
            pass

        toggle_move_button.configure(image=x_first_move_image)

    elif new_fm == 'o':
        o_first_move_image_active = PhotoImage(file="Images/o_first_move_active.png")
        o_first_move_label_active = Label(root, image=o_first_move_image_active, bg="#151326")
        o_first_move_label_active.pack()
        o_first_move_label_active.place(x=467.5, y=300, anchor=CENTER)
        
        try:
            x_first_move_label_active.place(x=1000, y=0)
        except:
            pass

        toggle_move_button.configure(image=o_first_move_image)

def check_fm():
    global wait
    if first_move == 'o':
        cpu_execution(random.randint(1,9), False)

def check_choices_valid():
    global submit_choices_button
    if difficulty == None and first_move == None:
        submit_choices_button.configure(image=submit_choices_err_image)
        flash_front_label(True, True)
        return
    elif first_move == None:
        submit_choices_button.configure(image=submit_choices_err_image)
        flash_front_label(True, False)
        return
    elif difficulty == None:
        submit_choices_button.configure(image=submit_choices_err_image)
        flash_front_label(False, True)
        return
    clear()
    slide()

x_pos_front_label = 337.5
next_appear = True
flash_front_label_ticker = 0

def flash_front_label(fm_label, diff_label):
    global x_pos_front_label, next_appear, flash_front_label_ticker, submit_choices_button
    flash_front_label_ticker += 1

    if next_appear == True:
        x_pos_front_label = 337.5
        next_appear = False
    else:
        x_pos_front_label = 1000
        next_appear = True

    if flash_front_label_ticker % 16 == 0:
        submit_choices_button.configure(image=submit_choices_image)
        return

    if fm_label == True:
        select_first_move_label.place(x=x_pos_front_label)
    if diff_label == True:
        select_difficulty_label.place(x=x_pos_front_label)
    root.after(100, lambda: flash_front_label(fm_label, diff_label))
    
wins = 0
ties = 0
losses = 0
slide_func_counter = 0

board_image = PhotoImage(file="Images/board.png")
board_label = Label(root, image=board_image, bg="#151326")
board_label.pack()
board_label.place(x=337.5, y=250, anchor=CENTER)

blank_button_1_image = PhotoImage(file="Images/blank_square_button.png")
blank_button_1 = Button(root, image=blank_button_1_image, highlightbackground="#151326", padx = 0, pady = 0, command=placed_x_1)
blank_button_1.place(x=204, y=117, anchor=CENTER)

blank_button_2_image = PhotoImage(file="Images/blank_square_button.png")
blank_button_2 = Button(root, image=blank_button_2_image, highlightbackground="#151326", padx = 0, pady = 0, command=placed_x_2)
blank_button_2.place(x=337.5, y=117, anchor=CENTER)

blank_button_3_image = PhotoImage(file="Images/blank_square_button.png")
blank_button_3 = Button(root, image=blank_button_3_image, highlightbackground="#151326", padx = 0, pady = 0, command=placed_x_3)
blank_button_3.place(x=471, y=117, anchor=CENTER)

blank_button_4_image = PhotoImage(file="Images/blank_square_button.png")
blank_button_4 = Button(root, image=blank_button_4_image, highlightbackground="#151326", padx = 0, pady = 0, command=placed_x_4)
blank_button_4.place(x=204, y=250, anchor=CENTER)

blank_button_5_image = PhotoImage(file="Images/blank_square_button.png")
blank_button_5 = Button(root, image=blank_button_5_image, highlightbackground="#151326", padx = 0, pady = 0, command=placed_x_5)
blank_button_5.place(x=337.5, y=250, anchor=CENTER)

blank_button_6_image = PhotoImage(file="Images/blank_square_button.png")
blank_button_6 = Button(root, image=blank_button_6_image, highlightbackground="#151326", padx = 0, pady = 0, command=placed_x_6)
blank_button_6.place(x=471, y=250, anchor=CENTER)

blank_button_7_image = PhotoImage(file="Images/blank_square_button.png")
blank_button_7 = Button(root, image=blank_button_7_image, highlightbackground="#151326", padx = 0, pady = 0, command=placed_x_7)
blank_button_7.place(x=204, y=383, anchor=CENTER)

blank_button_8_image = PhotoImage(file="Images/blank_square_button.png")
blank_button_8 = Button(root, image=blank_button_8_image, highlightbackground="#151326", padx = 0, pady = 0, command=placed_x_8)
blank_button_8.place(x=337.5, y=383, anchor=CENTER)

blank_button_9_image = PhotoImage(file="Images/blank_square_button.png")
blank_button_9 = Button(root, image=blank_button_9_image, highlightbackground="#151326", padx = 0, pady = 0, command=placed_x_9)
blank_button_9.place(x=471, y=383, anchor=CENTER)

easy_difficulty_image = PhotoImage(file="Images/diff_easy.png")
easy_button = Button(root, image=easy_difficulty_image, highlightbackground="#151326", padx = 0, pady = 0, command=lambda: difficulty_change('Easy'))
easy_button.place(x=127.5, y=500, anchor=CENTER)

med_difficulty_image = PhotoImage(file="Images/diff_medium.png")
med_button = Button(root, image=med_difficulty_image, highlightbackground="#151326", padx = 0, pady = 0, command=lambda: difficulty_change('Medium'))
med_button.place(x=267.5, y=500, anchor=CENTER)

hard_difficulty_image = PhotoImage(file="Images/diff_hard.png")
hard_button = Button(root, image=hard_difficulty_image, highlightbackground="#151326", padx = 0, pady = 0, command=lambda: difficulty_change('Hard'))
hard_button.place(x=407.5, y=500, anchor=CENTER)

impossible_difficulty_image = PhotoImage(file="Images/diff_impossible.png")
impossible_button = Button(root, image=impossible_difficulty_image, highlightbackground="#151326", padx = 0, pady = 0, command=lambda: difficulty_change("Impossible"))
impossible_button.place(x=547.5, y=500, anchor=CENTER)

clear_image = PhotoImage(file="Images/clear.png")
forfeit_image = PhotoImage(file="Images/forfeit.png")
forfeit_button = Button(root, image=forfeit_image, highlightbackground="#151326", padx = 0, pady = 0, command=forfeit_game)
forfeit_button.place(x=63, y=587, anchor=CENTER)

x_first_move_image = PhotoImage(file="Images/first_move_x.png")
o_first_move_image = PhotoImage(file="Images/first_move_o.png")
toggle_move_button = Button(root, image=x_first_move_image, highlightbackground="#151326", padx = 0, pady = 0, command=toggle_first_move)
toggle_move_button.place(x=612, y=587, anchor=CENTER)

record_label = Label(root, text=(str(wins) + ' - ' + str(losses) + ' - ' + str(ties)), bg="#151326", fg='#00a5ec', font=('system', 75))
record_label.place(x=337.5, y=575, anchor=CENTER)
# middle is y=587, without descriptors

record_descriptor = Label(root, text='Wins - Losses - Ties', bg="#151326", fg='#666666', font=('System', 15))
record_descriptor.place(x=337.5, y=625, anchor=CENTER)

# loss_descriptor = Label(root, text='Losses', bg="#151326", fg='#666666', font=('System', 15))
# loss_descriptor.place(x=337.5, y=625, anchor=CENTER)

# win_descriptor = Label(root, text='Wins', bg="#151326", fg='#666666', font=('System', 15))
# win_descriptor.place(x=224, y=625, anchor=CENTER)

# tie_descriptor = Label(root, text='Ties', bg="#151326", fg='#666666', font=('System', 15))
# tie_descriptor.place(x=451, y=625, anchor=CENTER)

cover_image = PhotoImage(file="Images/cover_image.png")
cover_label = Label(root, image=cover_image, highlightbackground="#151326", bg="#151326", padx=0, pady=0)
cover_label.place(x=0, y=0, anchor=NW)
# highlightbackground="#151326"

difficulty = None
first_move = None

easy_difficulty_image_front = PhotoImage(file="Images/diff_easy.png")
easy_button_front = Button(root, image=easy_difficulty_image, highlightbackground="#151326", padx = 0, pady = 0, command=lambda: difficulty_change('Easy'))
easy_button_front.place(x=127.5, y=500, anchor=CENTER)

med_difficulty_image_front = PhotoImage(file="Images/diff_medium.png")
med_button_front = Button(root, image=med_difficulty_image, highlightbackground="#151326", padx = 0, pady = 0, command=lambda: difficulty_change('Medium'))
med_button_front.place(x=267.5, y=500, anchor=CENTER)

hard_difficulty_image_front = PhotoImage(file="Images/diff_hard.png")
hard_button_front = Button(root, image=hard_difficulty_image, highlightbackground="#151326", padx = 0, pady = 0, command=lambda: difficulty_change('Hard'))
hard_button_front.place(x=407.5, y=500, anchor=CENTER)

impossible_difficulty_image_front = PhotoImage(file="Images/diff_impossible.png")
impossible_button_front = Button(root, image=impossible_difficulty_image, highlightbackground="#151326", padx = 0, pady = 0, command=lambda: difficulty_change("Impossible"))
impossible_button_front.place(x=547.5, y=500, anchor=CENTER)

submit_choices_err_image = PhotoImage(file="Images/submit_customs_err.png")
submit_choices_image = PhotoImage(file="Images/submit_customs.png")
submit_choices_button = Button(root, image=submit_choices_image, bg='#151326', highlightbackground="#151326", pady=0, padx=0, command=lambda: check_choices_valid())
submit_choices_button.place(x=337.5, y=600, anchor=CENTER)

select_difficulty_image = PhotoImage(file="Images/select_difficulty.png")
select_difficulty_label = Label(root, image=select_difficulty_image, highlightbackground="#151326", bg="#151326")
select_difficulty_label.place(x=337.5, y=450, anchor=CENTER)

select_first_move_image = PhotoImage(file="Images/select_first_move.png")
select_first_move_label = Label(root, image=select_first_move_image, highlightbackground="#151326", bg="#151326")
select_first_move_label.place(x=337.5, y=250, anchor=CENTER)

x_first_move_image_front = PhotoImage(file="Images/x_first_move.png")
x_first_move_label_front = Button(root, image=x_first_move_image_front, highlightbackground="#151326", bg="#151326", padx=0, pady=0, command=lambda: change_fm('x'))
x_first_move_label_front.place(x=207.5, y=300, anchor=CENTER)

o_first_move_image_front = PhotoImage(file="Images/o_first_move.png")
o_first_move_label_front = Button(root, image=o_first_move_image_front, highlightbackground="#151326", bg="#151326", padx=0, pady=0, command=lambda: change_fm('o'))
o_first_move_label_front.place(x=467.5, y=300, anchor=CENTER)

ttt_title_image = PhotoImage(file="Images/tictactoe.png")
ttt_title = Label(root, image=ttt_title_image, highlightbackground="#151326", bg="#151326")
ttt_title.place(x=337.5, y=75, anchor=CENTER)

root.mainloop()
