#Code by Christine Polly Paul
import csv


def readcsv(file):
    reader = csv.reader(open(file), delimiter=';')
    recordbas = []
    for row in reader:
        recordbas.append(row)
    return recordbas


recordb,recordh = [], []

filename = "basketball.csv"
recordb = readcsv(filename)
filename = "handball.csv"
recordh = readcsv(filename)

def game_record(data, fo):
    recor = []
    record = []
    if fo == "PLAYER":
        for index, row in enumerate(data):
            recor.append(data[index][0:4])
            test_tup2 = recor[index]
            test_tup1 = ('player name', 'nickname', 'number', 'team name')
            res = dict(zip(test_tup1, test_tup2))
            record.append(res)
            record[index]['points'] = 0

    elif fo == "BASKETBALL":
        for index, row in enumerate(data):
            recor.append(data[index][4:])
            test_tup2 = recor[index]
            test_tup1 = ('position', 'scored points', 'rebounds', 'assists')
            res = dict(zip(test_tup1, test_tup2))
            record.append(res)
            record[index]['game'] = 'basketball'


    elif fo == "HANDBALL":
        for i, r in enumerate(data):
            recor.append(data[i][4:])
            test_tup2 = recor[i]
            test_tup1 = ('position', 'goals made', 'goals received')
            res = dict(zip(test_tup1, test_tup2))
            record.append(res)
            record[i]['game'] = 'handball'

    return record

basketballrecord = []
handballrecord = []
player = []

h = "HANDBALL"
handballrecord = game_record(recordh, h)

b = "BASKETBALL"
basketballrecord = game_record(recordb, b)

p = "PLAYER"
player = game_record(recordb, p)


def displayrecord(data):
    for index, row in enumerate(data):
        print(data[index])


def team_winning(data):
    ascore = 0
    bscore = 0
    for j, k in enumerate(data):
        if str(data[j].get('game')) == 'handball':
            if str(player[j].get('team name')) == 'TeamA':
                ascore += int(data[j].get('goals made'))
            if str(player[j].get('team name')) == 'TeamB':
                bscore += int(data[j].get('goals made'))
        if str(data[j].get('game')) == 'basketball':
            if str(player[j].get('team name')) == 'TeamA':
                ascore += int(data[j].get('scored points'))
            if str(player[j].get('team name')) == 'TeamB':
                bscore += int(data[j].get('scored points'))
    if ascore > bscore:
        w = "Team A"
    else:
        w = "Team B"
    return w


def addpoints(team, data):
    x , y = 0, 0
    if team == 'Team A':
        for x, y in enumerate(data):
            if data[x].get('team name') == 'TeamA':
                data[x].update({"points": int(data[x].get('points')) + 10})
    if team == 'Team B':
        for x, y in enumerate(data):
            if data[x].get('team name') == 'TeamB':
                data[x].update({"points": int(data[x].get('points')) + 10})


def cal_ratingpoints(data,bdata,hdata):
    a = 0
    for q, u in enumerate(data):
        if hdata[q].get('position') == 'G' and hdata[q].get('game') == 'handball':
            a = 50 + int(hdata[q].get('goals made'))*5 - int(hdata[q].get('goals received'))*2
            data[q].update({"points": int(data[q].get('points')) + a})
            a = 0
        if hdata[q].get('position') == 'F'and hdata[q].get('game') == 'handball':
            a = 20 + (int(hdata[q].get('goals made'))*1) - (int(hdata[q].get('goals received'))*1)
            data[q].update({"points": (int(data[q].get('points')) + a)})
            a = 0
        if bdata[q].get('position') == 'G' and bdata[q].get('game') == 'basketball':
            a = int(bdata[q].get('scored points'))*2 + int(bdata[q].get('rebounds'))*3 + int(bdata[q].get('assists'))*1
            data[q].update({"points": int(data[q].get('points')) + a})
            a = 0
        if bdata[q].get('position') == 'F' and bdata[q].get('game') == 'basketball':
            a = int(bdata[q].get('scored points')) * 2 + int(bdata[q].get('rebounds')) * 2 + int(bdata[q].get('assists')) *2
            data[q].update({"points": int(data[q].get('points')) + a})
            a = 0
        if bdata[q].get('position') == 'C' and bdata[q].get('game') == 'basketball':
            a = (int(bdata[q].get('scored points'))*2) + (int(bdata[q].get('rebounds'))*1) + (int(bdata[q].get('assists'))*3)
            data[q].update({"points": int(data[q].get('points')) + a})
            a = 0


cal_ratingpoints(player,basketballrecord,handballrecord)


winner = team_winning(handballrecord)

addpoints(winner, player)


winner = team_winning(basketballrecord)

addpoints(winner, player)


def player_winning():
    a = 0
    f = ''
    for j, k in enumerate(player):
        if a < int(player[j].get('points')):
             a = int(player[j].get('points'))
             f = str(player[j].get('player name'))

    for s, v in enumerate(player):
        if f == str(player[s].get('player name')):
            print('The most valued player is:')
            print(player[s])
            print(basketballrecord[s])
            print(handballrecord[s])
    return a


mvp = player_winning()


# Output
# The most valued player is:
# {'player name': 'player3', 'nickname': 'nick3', 'number': '15', 'team name': 'TeamA', 'points': 72}
# {'position': 'C', 'scored points': '15', 'rebounds': '10', 'assists': '4', 'game': 'basketball'}
# {'position': 'F', 'goals made': '10', 'goals received': '20', 'game': 'handball'}
#
# Process finished with exit code 0


