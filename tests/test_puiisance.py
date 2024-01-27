import pytest
import puissance_4 as ps

def test_place_red():
    game = ps.Game()
    game.place_mark(2,'R')
    assert(game.grid[5][2] == 'R')

def test_place_two_reds_on_top():
    game = ps.Game()
    game.place_mark(2,'R')
    game.place_mark(2,'R')
    assert(game.grid[4][2] == 'R')
    assert(game.grid[5][2] == 'R')

def test_place_yellow():
    game = ps.Game()
    game.place_mark(2,'Y')
    assert(game.grid[5][2] == 'Y')

def test_place_one_yellow_one_red_horizontal():
    game = ps.Game()
    game.place_mark(1,'Y')
    game.place_mark(2,'R')
    assert(game.grid[5][2] == 'R')
    assert(game.grid[5][1] == 'Y')

def test_place_one_yellow_one_red_vertical():
    game = ps.Game()
    game.place_mark(1,'Y')
    game.place_mark(1,'R')
    assert(game.grid[4][1] == 'R')
    assert(game.grid[5][1] == 'Y')

def test_place_four_aligned_reds_vertical():
    game = ps.Game()
    game.place_mark(1,'R')
    game.place_mark(1,'R')
    game.place_mark(1,'R')
    assert(game.place_mark(1,'R') == True)

def test_place_four_aligned_reds_horizontal():
    game = ps.Game()
    game.place_mark(0,'R')
    game.place_mark(1,'R')
    game.place_mark(2,'R')
    assert(game.place_mark(3,'R') == True)

def test_place_three_aligned_reds_horizontal_and_one_red_last_inordered():
    game = ps.Game()
    game.place_mark(0,'R')
    game.place_mark(1,'R')
    game.place_mark(6,'R')
    assert(game.place_mark(2,'R') == False)

def test_place_four_aligned_reds_horizontal_not_in_order():
    game = ps.Game()
    game.place_mark(0,'R')
    game.place_mark(1,'R')
    game.place_mark(3,'R')
    print('last---')
    x=game.place_mark(2,'R')
    print(game)
    assert(x == True)

def test_place_five_reds_horizontal_with_hole():
    game = ps.Game()
    game.place_mark(0,'R')
    game.place_mark(1,'R')
    game.place_mark(4,'R')
    game.place_mark(5,'R')
    x=game.place_mark(2,'R')
    print(game)
    assert(x == False)

def test_place_four_reds_horizontal_with_hole():
    game = ps.Game()
    game.place_mark(0,'R')
    game.place_mark(1,'R')
    game.place_mark(4,'R')
    x=game.place_mark(2,'R')
    print(game)
    assert(x == False)

def test_place_three_aligned_reds_horizontal_and_one_yellow():
    game = ps.Game()
    game.place_mark(0,'Y')
    game.place_mark(1,'R')
    game.place_mark(2,'R')
    assert(game.place_mark(3,'R') == False)

def test_place_four_aligned_reds_vertical():
    game = ps.Game()
    game.place_mark(0,'Y')
    game.place_mark(1,'R')
    game.place_mark(1,'R')
    game.place_mark(1,'R')
    # print(game)
    # assert(False)
    assert(game.place_mark(1,'R') == True)

def test_place_four_unaligned_reds_vertical():
    game = ps.Game()
    game.place_mark(0,'R')
    game.place_mark(1,'Y')
    game.place_mark(1,'R')
    game.place_mark(1,'R')
    assert(game.place_mark(1,'R') == False)

def test_place_four_aligned_red_first_diagonal():
    game = ps.Game()
    game.place_mark(0,'R')
    game.place_mark(1,'Y')
    game.place_mark(1,'R')
    game.place_mark(2,'Y')
    game.place_mark(2,'Y')
    game.place_mark(2,'R')
    game.place_mark(3,'R')
    game.place_mark(3,'Y')
    game.place_mark(3,'R')
    # print(game)
    assert(game.place_mark(3,'R') == True)

def test_place_four_unaligned_red_first_diagonal():
    game = ps.Game()
    game.place_mark(0,'R')
    game.place_mark(1,'Y')
    game.place_mark(1,'R')
    game.place_mark(2,'Y')
    game.place_mark(2,'Y')
    game.place_mark(3,'R')
    game.place_mark(3,'Y')
    game.place_mark(3,'R')
    game.place_mark(3,'Y')
    game.place_mark(4,'R')
    game.place_mark(4,'Y')
    game.place_mark(4,'R')
    game.place_mark(4,'Y')
    game.place_mark(4,'R')
    x = game.place_mark(2,'R')
    # print(game)
    assert(x == False)

def test_place_four_aligned_red_second_diagonal():
    game = ps.Game()
    game.place_mark(3,'R')
    game.place_mark(2,'Y')
    game.place_mark(2,'R')
    game.place_mark(1,'Y')
    game.place_mark(1,'Y')
    game.place_mark(1,'R')
    game.place_mark(0,'R')
    game.place_mark(0,'Y')
    game.place_mark(0,'R')
    x = game.place_mark(0,'R')
    print(game)
    assert( x == True)
