# Python-Code-MVP

Tournament Most Valuable Player calculation
Problem
Tucan Tournament is a tournament where several players compete in several sports. Right now, the sports played are basketball and handball games. They plan to add more sports in the future.

You have been contacted to create a program to calculate the Most Valuable Player (MVP) of the tournament.

You will receive a set of files, each one containing the stats of one game. Each file will start with a row indicating the sport it refers to.

Each player is assigned a unique nickname. Each file represent a single game. The MVP is the player with the most rating points, adding the rating points in all games.

A player will receive 10 additional rating points if their team won the game. Every game must have a winner team. One player may play in different teams and positions in different games, but not in the same game.

Basketball

Each row will represent one player stats, with the format: player name;nickname;number;team name;position;scored points;rebounds;assists

This table details the rating points each player in a basketball game receives depending on her position:

Position	Score	Rebounds	Assists
Guard(G)	2	3	1
Forward(F)	2	2	2
Center(C)	2	1	3
E.g. a player playing as center with 10 scored points, 5 rebounds and no assists will be granted 25 rating points (10*2 + 5*1 + 0*3).

The winner team is the one with more scored points.

Handball

Each row will represent one player stats, with the format: player name;nickname;number;team name;position;goals made;goals received

This table details the rating points each player in a handball game receives depending on her position:

Position	Initial points	Goals made	Goals received
Goalkeeper(G)	50	5	-2
Field player(F)	20	1	-1
E.g. a player playing as goalkeeper with 1 goals made and 10 received will be granted 35 rating points (50 + 1*5 ­ 10*2 = 35).

The winner team is the one with more goals made.
