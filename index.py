board = [0,1,2,3,4,5,6,7,8]
xWin = 0
oWin = 0
def show():
    print "_____________"
    print '|',board[0],'|',board[1],'|',board[2],'|'
    print "_____________"
    print '|',board[3],'|',board[4],'|',board[5],'|'
    print "_____________"
    print '|',board[6],'|',board[7],'|',board[8],'|'
    print "_____________"
show()
print "The Tic Tac Toe Board looks like the one above. Each square has a number which is a position. The program keeps providing inputs for the user to select that position. You both have a total of nine turns to beat your opponent. X starts the game. Good Luck!"
turn = 1
turns = 0
while turns < 9:
    pos = int(input("Enter a position"))
    if pos >= 9:
        print "You were supposed to enter out a number between zero and eight"
    realTurn = turn%2
    if realTurn == 0:
        board[pos] = 'o'
    else:
        board[pos] = 'x'
    print "You have %i turns left" % turn
    show()
    turns += 1
    turn += 1
    if board[0] == 'x' and board[1] == 'x' and board[2] == 'x':
        print "X WINS"
        break
    elif board[3] == 'x' and board[4] == 'x' and board[5] == 'x':
        print "X WINS"
        break
    elif board[6] == 'x' and board[7] == 'x' and board[8] == 'x':
        print "X WINS"
        break
    elif board[0] == 'x' and board[3] == 'x' and board[6] == 'x':
        print "X WINS"
        break
    elif board[1] == 'x' and board[4] == 'x' and board[7] == 'x':
        print "X WINS"
        break
    elif board[2] == 'x' and board[5] == 'x' and board[8] == 'x':
        print "X WINS"
        break
    elif board[0] == 'x' and board[4] == 'x' and board[8] == 'x':
        print "X WINS"
        break
    elif board[2] == 'x' and board[4] == 'x' and board[6] == 'x':
        print "X WINS"
        break
    if board[0] == 'o' and board[1] == 'o' and board[2] == 'o':
        print "O WINS"
        break
    elif board[3] == 'o' and board[4] == 'o' and board[5] == 'o':
        print "O WINS"
        break
    elif board[6] == 'o' and board[7] == 'o' and board[8] == 'o':
        print "O WINS"
        break
    elif board[0] == 'o' and board[3] == 'o' and board[6] == 'o':
        print "O WINS"
        break
    elif board[1] == 'o' and board[4] == 'o' and board[7] == 'o':
        print "O WINS"
        break
    elif board[2] == 'o' and board[5] == 'o' and board[8] == 'o':
        print "O WINS"
        break
    elif board[0] == 'o' and board[4] == 'o' and board[8] == 'o':
        print "O WINS"
        break
    elif board[2] == 'o' and board[4] == 'o' and board[6] == 'o':
        print "O WINS"
        break
