# Lightning-chess-engine-1.1
A chess engine built on a simple Alpha-Beta and a Quiesce search, with null move and piece tables evaluation.  This chess engine is based on code from https://andreasstckl.medium.com/writing-a-chess-program-in-one-day-30daff4610ec. However, I had added a more suitable UI and endgame "evaluation" that currently only consists of an endgame king table and a gaviota database for probing. Also note that this chess engine uses a library from python called python-chess, which provides it with basic move generation and others.

TEST GAMES AGAINST STOCKFISH:
With my engine as white
g1f3
g8f6
b1c3
b8c6
e2e4
e7e5
d2d4
e5d4
f3d4
f8b4
d4c6
b4c3
b2c3
d7c6
d1d8
e8d8
c1g5
c8g4
g5f6
g7f6
f1d3
d8c8
e1g1
h8g8
g1h1
c8b8
f1e1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
h1g1
e8g8
g1h1
g8e8
1/2 - 1/2
My program: Depth of 5
Stockfish: time to think 5 seconds 

Unfortunately my program did not realise that this has already suppressed the three penfold draw!
