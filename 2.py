def make():
    return

def run(game, n):
    
    current = n
    if max(game[0]['meetLine1'], game[0]['meetLine2'] ) == current:
        current = current - 1   
    elif min(game[0]['meetLine1'], game[0]['meetLine2']) == current:
        current = current + 1
    
    return current

# def test_column2_row0():
    
#     assert 1 == run(game, 1)
#     assert 2 == run(game, 2)
########
def test_column2_row1():
    game = [{'meetLine1' : 1, 'meetLine2' : 2}]
    assert 2 == run(game, 1)
    assert 1 == run(game, 2)
######## 3
# def test_column2_row2():
#     [game = {'meetLine1' : 1, 'meetLine' :2}]
#     assert 1 == run(game, 1)
#     assert 2 == run(game, 2)
# ###
def test_column3_row2():
    game = [{'meetLine1' : 1, 'meetLine2' : 2}, {'meetLine1' : 2, 'meetLine2' : 3}]
    
    assert run(game, 1) == 2
    assert run(game, 2) == 1
    assert run(game, 3) == 3

#test_column3_row2()

def test_column3_row1():
    game = [{'meetLine1' : 2, 'meetLine2' : 3}]
    
    assert run(game, 1) == 1
    assert run(game, 2) == 3
    assert run(game, 3) == 2