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

def test_all_locations():
    # Replace with tests

def test_adjacent_location():
    # Replace with tests
    
def test_is_legal_move_by_musketeer():
    # Replace with tests
    
def test_is_legal_move_by_enemy():
    # Replace with tests

def test_is_legal_move():
    # Replace with tests

def test_can_move_piece_at():
    # Replace with tests

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    # Replace with tests

def test_is_legal_location():
    # Replace with tests

def test_is_within_board():
    # Replace with tests

def test_all_possible_moves_for():
    # Replace with tests
    
def test_make_move():
    # Replace with tests
    
def test_choose_computer_move():
    # Replace with tests; should work for both 'M' and 'R'

def test_is_enemy_win():
    # Replace with tests


