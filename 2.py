import random

def make(column, row):
    game = []
    for i in range (0,row):
        x = random.randrange(1,column)
        game.append({'meetLine1' : x, 'meetLine2' : x+1})
    
    return game

def make2(column, row):
    game = []
    # 모든 컬럼이 연결이 되도록 기본 로우를 할당한다.
    if row < column-1:
        row = column-1
    for i in range(1, column):
        game.append({'meetLine1' : i, 'meetLine2' : i+1})
    row -= column-1

    # 나머지 로우를 할당한다.
    for i in range (0,row):
        x = random.randrange(1,column)
        game.append({'meetLine1' : x, 'meetLine2' : x+1})

    # 앞부분 순서가 고정이어서 섞어준다.
    random.shuffle(game)
    
    return game

def print_game(game):
    for row in game:
        for column in range(0, 20):
            print('I',end='')
            if row['meetLine1'] == column+1:
                print('-', end='')
            else:
                print(' ', end='')
        print(' ')

def run(game, n):
    
    current = n
    for i in range (0, len(game)):
        if max(game[i]['meetLine1'], game[i]['meetLine2'] ) == current:
            current = current - 1   
        elif min(game[i]['meetLine1'], game[i]['meetLine2']) == current:
            current = current + 1
    
    return current

def test_column2_row0():
    game = []
    assert 1 == run(game, 1)
    assert 2 == run(game, 2)

def test_column2_row1():
    game = [{'meetLine1' : 1, 'meetLine2' : 2}]
    assert 2 == run(game, 1)
    assert 1 == run(game, 2)

def test_column2_row2():
    game = [{'meetLine1' : 1, 'meetLine2' :2}, {'meetLine1' : 1, 'meetLine2' : 2}]
    assert 1 == run(game, 1)
    assert 2 == run(game, 2)

def test_column3_row2():
    game = [{'meetLine1' : 1, 'meetLine2' : 2}, {'meetLine1' : 2, 'meetLine2' : 3}]
    
    assert run(game, 1) == 3
    assert run(game, 2) == 1
    assert run(game, 3) == 2


def test_column3_row1():
    game = [{'meetLine1' : 2, 'meetLine2' : 3}]
    
    assert run(game, 1) == 1
    assert run(game, 2) == 3
    assert run(game, 3) == 2
    
def test_complex():
    game = [{'meetLine1' : 1, 'meetLine2' : 2}, {'meetLine1' :3, 'meetLine2' : 4}, {'meetLine1' : 2, 'meetLine2' : 3}, {'meetLine1' : 3, 'meetLine2' : 2}, {'meetLine1' : 2, 'meetLine2' : 1}]
    
    assert run(game, 1) == 1
    assert run(game, 2) == 2
    assert run(game, 3) == 4
    assert run(game, 4) == 3

def test_make_21():
    game = make(2, 1)
    assert game[0]['meetLine1'] == 1
    assert game[0]['meetLine2'] == 2
   

def test_make_820():
    game = make(8, 20)
    print_game(game)
    assert game[0]['meetLine1'] == 1
    assert game[0]['meetLine2'] == 2
    assert game[1]['meetLine1'] == 1
    assert game[1]['meetLine2'] == 2
    assert run(game, 1) == 1
    assert run(game, 2) == 2

if __name__=='__main__':
    column = 8
    for row_count in range (column-1, 50):
        data = []
        results = [[0 for x in range(column+1)] for y in range(column+1)] 
        results_percent = [[0 for x in range(column+1)] for y in range(column+1)] 
        count_11 = 0
        iteration = 10000
        for x in range(0,iteration):
            game = make2(column,row_count)
            for i in range (1,column+1):
                result = run(game,i)
                #print('선택:',i, '결과:', result)
                # data.append({'선택' : i, '결과' : result})
            
                # if data[8*x+(i-1)]['선택'] == 1:
                #     if result == 3:
                #         #print(i,result)
                #         count_11 += 1

                results[i][result] += 1
        results_percent = [[int(x/iteration*100) for x in y] for y in results]

        print(row_count, results_percent)
        #print(row_count, results, results_percent)
       # print(row_count, ' ', count_11, ' ', count_11/1000*100)