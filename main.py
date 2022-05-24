import random

### Дилемма заключенного 
## Оба молчат - 1 год тюрьмы обоим;
## Один молчит, другой сдаёт - одному 10 лет тюрьмы, другого отпускают
## Оба сдают - 5 лет тюрьмы обоим
#score = {'00': -1, '01': -10, '10': 0, '11': -5}
### Один загадывает чёт/нечёт, второй угадывает
## 
#score = {'00': 1, '01': 5, '10': 5, '11': 1}
## Ты мне, я тебе 
# Оба обменялись подарками - 3 очка каждому
# Первый дал подарок, второй нет - первому 0 очков, второму 5 очков
# Оба не обменялись подарками - 1 очко каждому
score = {'00': 1, '01': 5, '10': 0, '11': 3}

def strategy1(prevmoves, oppprevmoves):
    return 1

def strategy2(prevmoves, oppprevmoves):
    return 0

def strategy3(prevmoves, oppprevmoves):
    try:
        return oppprevmoves[-1]
    except:
        return 1

def strategy4(prevmoves, oppprevmoves):
    try:
        return oppprevmoves[-1]
    except:
        return 0 

def strategy5(prevmoves, oppprevmoves):
    try:
        return oppprevmoves[-1]
    except:
        return random.randint(0, 1) 

def main():
    players = {'player1': strategy1,
               'player2': strategy2,
               'player3': strategy3,
               'player4': strategy4,
               'player5': strategy5,
              } 
    players_cnt = len(players)
    games_cnt = 10
    res_score = {}
    for i in range(1, players_cnt + 1):
        for j in range(i, players_cnt + 1):
            imoves = []
            jmoves = []
            iscore = 0
            jscore = 0
            pi = f'player{i}' 
            pj = f'player{j}' 
            for k in range(1, games_cnt + 1):
                ires = players[pi](imoves, jmoves) 
                jres = players[pj](jmoves, imoves) 
                imoves.append(ires)
                jmoves.append(jres)
                iscore += score[f'{ires}{jres}']
                jscore += score[f'{jres}{ires}']
                #print(f'Game number - {k}: {pi} vs {pj}')
                #print(imoves, jmoves)
            print(f'{pi} vs {pj} = {iscore} : {jscore}')
            if pi in res_score:
                res_score[pi] += iscore
            else:
                res_score[pi] = iscore
            if pj in res_score:
                if i != j: res_score[pj] += iscore
            else:
                res_score[pj] = iscore
    res_list = list(res_score.items())
    res_list.sort(key=lambda x: x[1], reverse=True)
    print(res_list)

if __name__ == '__main__':
    main()
