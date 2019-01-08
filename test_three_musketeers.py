import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 =  [ [_, _, _, _, _],
            [_, _, _, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board3 =  [ [_, _, _, _, _],
            [_, _, _, _, _],
            [_, _, M, _, _],
            [_, _, _, _, M],
            [_, _, _, M, R] ]

board4 =  [ [_, _, _, R, _],
            [_, _, R, _, _],
            [_, R, _, _, M],
            [_, R, _, M, _],
            [_, _, _, M, _] ]

board5 =  [ [_, _, _, _, _],
            [_, _, _, _, _],
            [_, _, _, _, M],
            [_, _, _, M, R],
            [_, _, _, M, _] ]

board6 =  [ [_, _, _, _, _],
            [_, _, _, _, M],
            [_, _, _, _, _],
            [_, _, _, M, R],
            [_, _, _, M, _] ]

board7 =  [ [_, _, _, _, _],
            [_, _, _, M, _],
            [_, _, _, _, _],
            [_, _, _, M, R],
            [_, _, _, M, _] ]

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases
    assert at((2, 2)) == M
    assert at((3, 3)) == R

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M
    #eventually add some board2 and at least 3 tests with it
    set_board(board2)
    assert at((0, 3)) == _
    assert at((1, 2)) == _
    assert at((3, 3)) == R

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board
    set_board(board2)
    assert board2 == get_board()

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
        string_to_location('T68')
    assert string_to_location('A1') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs
    with pytest.raises(ValueError):
        string_to_location('$:^')
    assert string_to_location('A2') == (0, 1)
    assert string_to_location('D4') == (3, 3)

def test_location_to_string():
    with pytest.raises(ValueError):
    # Replace with tests
        location_to_string((6,6))
        location_to_string((2,6))
    assert location_to_string((0,0)) == 'A1'
    assert location_to_string((4,4)) == 'E5'

def test_at():
    # Replace with tests
    set_board(board1)
    with pytest.raises(ValueError):
        at((7, 8))
        at((1, 35))
    assert at((0, 0)) == _
    assert at((1, 2)) == R
    assert at((2, 2)) == M
    

def test_all_locations():
    # Replace with tests
    allocations = []
    for i in range (0,5):
        for j in range (0,5):
            allocations.append((i,j))
    assert test_all_locations() == allocations


def test_adjacent_location():
    # Replace with tests
    with pytest.raises(ValueError):
        adjacent_location((1,0),up)
        adjacent_location((4,2),down)
        adjacent_location((0,0),left)
        adjacent_location((0,4),right)
    assert adjacent_location((0,0),right) == (0,1)
    assert adjacent_location((1,2),down) == (2,2)
    assert adjacent_location((4,3),left) == (4,2)
    assert adjacent_location((3,3),up) == (2,3)
    
def test_is_legal_move_by_musketeer():
    # Replace with tests
    with pytest.raises(ValueError):
        at(location) != 'M'
    set_board(board1)
    assert is_legal_move_by_musketeer((0,3),down) == False
    assert is_legal_move_by_musketeer((1,3),left) == True
    assert is_legal_move_by_musketeer((2,2),right) == True
    
def test_is_legal_move_by_enemy():
    # Replace with tests
    with pytest.raises(ValueError):
        at(location) != 'R'
    set_board(board1)
    assert is_legal_move_by_enemy((1,2),right) == False
    assert is_legal_move_by_enemy((1,2),left) == True
    assert is_legal_move_by_enemy((3,1),up) == False

def test_is_legal_move():
    # Replace with tests
    set_board(board1)
    assert is_legal_move((2,2), right) == True
    assert is_legal_move((2,2), down) == False
    assert is_legal_move((2,1), right) == False
    assert is_legal_move((2,1), up) == True

def test_can_move_piece_at():
    # Replace with tests
    set_board(board1)
    assert can_move_piece_at((0,3)) == False
    assert can_move_piece_at((1,3)) == True
    assert can_move_piece_at((2,1)) == True

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board
    set_board(board3)
    assert has_some_legal_move_somewhere('R') == False
    assert has_some_legal_move_somewhere('M') == True
    set_board(board4)
    assert has_some_legal_move_somewhere('R') == True
    assert has_some_legal_move_somewhere('M') == False

def test_possible_moves_from():
    # Replace with tests
    set_board(board1)
    assert possible_moves_from((0,0)) == []
    assert possible_moves_from((1,3)) == ['left']
    assert possible_moves_from((2,2)) == ['up','left','right']

def test_is_legal_location():
    # Replace with tests
    assert is_legal_location((5,5)) == False
    assert is_legal_location((1,5)) == False
    assert is_legal_location((1,4)) == True

def test_is_within_board():
    # Replace with tests
    assert within_board((0,0), left) == False
    assert within_board((3,3), right) == True
    assert within_board((2,2), up) == True
    assert within_board((4,1), down) == False

def test_all_possible_moves_for():
    # Replace with tests
    set_board(board1)
    assert all_possible_moves_for(M) == [
            ((1,3), 'left'),
            ((1,3), 'down'),
            ((2,2), 'left'),
            ((2,2), 'up'),
            ((2,2), 'right')]
    set_board(board3)
    assert all_possible_moves_for(M) == [
            ((3,4),'down'),
            ((4,3),'right')]
    
def test_make_move():
    # Replace with tests
    make_move(location, direction)
    assert at(location) == '-'

def test_choose_computer_move():
    # Replace with tests; should work for both 'M' and 'R'
    set_board(board5)
    assert choose_computer_move(R) == ((3,4),'down')
    set_board(board6)
    assert choose_computer_move(M) == ((3,3),'right')
        

def test_is_enemy_win():
    # Replace with tests
    set_board(board1)
    assert is_enemy_win() == False
    set_board(board7)
    assert is_enemy_win() == True