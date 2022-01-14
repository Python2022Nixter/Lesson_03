# Tic Tac Toe Game
# Закончено ! Работает !


player1 = "X"
player2 = "O"
playerMove = True


def create_board():
    board = []
    for i in range(3):
        board.append(["."] * 3)
    return board


def create_board_numbers():
    board = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    return board


def pr_matrix(matrix):
    for row in matrix:   
        print(*row)
# def pr_matrix(matrix):
#     lst = []
#     str = """
#     {} | {} | {}
#     {} | {} | {}
#     {} | {} | {}\r""".format(*matrix[0], *matrix[1], *matrix[2])
#     for row in matrix:
#         for col in row:
#             lst.append(col)
#             #print(col, end="")
#     print(str + '\r')

board = create_board()
board_numbers = create_board_numbers()
print("Game Board:")
pr_matrix(board_numbers)


def check_empty_cells(board):
    '''
    Проверяет есть ли пустые клетки на доске
    '''
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                return True
    return False




def get_cell_index(cell_number):
    '''
    Взятие индекса ячейки по номеру
    '''
    for i in range(3):
        for j in range(3):
            if board_numbers[i][j] == cell_number:
                return i, j



def set_cell_value(cell_number, value):
    '''
    Установка Х или О в ячейку
    '''
    global board
    i, j = cell_number
    board[i][j] = value

# Проверить пустая ли ячейка
def check_cell_empty(cell_number):
    i, j = cell_number
    if board[i][j] == ".":
        return True
    else:
        return False


# Проверить выиграл ли кто-то
def check_winner(board, player):
    '''
    Проверка выиграл ли кто-то
    '''
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


while check_empty_cells(board):
    '''
    Game loop
    '''
    if playerMove:
        playerMove = False
        print("Player 1 move:")
        i = int(input("Enter number of cell: "))
        cell_path = get_cell_index(i)
        if check_cell_empty(cell_path):
            set_cell_value(cell_path, player1)
        if check_winner(board, player1):
            print("Player 1 win!")
            pr_matrix(board)
            break
        pr_matrix(board)
    else:
        playerMove = True
        print("Player 2 move:")
        i = int(input("Enter number of cell: "))
        cell_path = get_cell_index(i)
        if check_cell_empty(cell_path):
            set_cell_value(cell_path, player2)
        if check_winner(board, player2):
            print("Player 2 win!")
            pr_matrix(board)
            break
        pr_matrix(board)
