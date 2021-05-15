import othello
import players

def main(first_player, second_player):
    board = othello.generate(size = 8)
    is_on_playing = True
    while is_on_playing:
        is_move_done = False
        options = othello.optionsOf(board, 1)
        if options:
            pos = first_player.optFor(board, 1)
            othello.move(board,1,pos,inplace=True)
            is_move_done = True
        options = othello.optionsOf(board, -1)
        if options:
            pos = second_player.optFor(board, -1)
            othello.move(board,-1,pos,inplace=True)
            is_move_done = True
        is_on_playing = is_move_done
    nb, nw = othello.count(board)
    if nb > nw:
        return 1
    elif nb < nw:
        return -1
    return 0

if __name__ == '__main__':
    first_player = players.RandomPlayer
    second_player = players.RandomPlayer
    count = {-1:0,1:0,0:0}
    for i in range(100):
        win = main(first_player, second_player)
        count[win] += 1
    print(count)
