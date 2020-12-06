import chess
import chess.engine
import random
import chess.svg
import chess.polyglot
import asyncio
import chess.engine
import time
color = input("what color do you want to be?")
game = "middlegame"
from IPython.display import SVG
board = chess.Board()
print (board)
move = 0
chess.svg.piece(chess.Piece.from_symbol("R"))
chess.svg.piece(chess.Piece.from_symbol("r"))
chess.svg.piece(chess.Piece.from_symbol("Q"))
chess.svg.piece(chess.Piece.from_symbol("q"))
chess.svg.piece(chess.Piece.from_symbol("K"))
chess.svg.piece(chess.Piece.from_symbol("k"))
chess.svg.piece(chess.Piece.from_symbol("P"))
chess.svg.piece(chess.Piece.from_symbol("p"))
chess.svg.piece(chess.Piece.from_symbol("N"))
chess.svg.piece(chess.Piece.from_symbol("n"))

chess.svg.piece(chess.Piece.from_symbol("B"))
chess.svg.piece(chess.Piece.from_symbol("b"))  
pawntable = [
0,  0,  0,  0,  0,  0,  0,  0,
5, 10, 10,-20,-20, 10, 10,  5,
5, -5,-10,  0,  0,-10, -5,  5,
0,  0,  0, 20, 20,  0,  0,  0,
5,  5, 10, 25, 25, 10,  5,  5,
10, 10, 20, 30, 30, 20, 10, 10,
50, 50, 50, 50, 50, 50, 50, 50,
0,  0,  0,  0,  0,  0,  0,  0]

knightstable = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  5,  5,  0,-20,-40,
-30,  5, 10, 15, 15, 10,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 10, 15, 15, 10,  0,-30,
-40,-20,  0,  0,  0,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]

bishopstable = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  5,  0,  0,  0,  0,  5,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10,-10,-10,-10,-10,-20]

rookstable = [
0,  0,  0,  5,  5,  0,  0,  0,
-5,  0,  0,  0,  0,  0,  0, -5,
-5,  0,  0,  0,  0,  0,  0, -5,
-5,  0,  0,  0,  0,  0,  0, -5,
-5,  0,  0,  0,  0,  0,  0, -5,
-5,  0,  0,  0,  0,  0,  0, -5,
5, 10, 10, 10, 10, 10, 10,  5,
0,  0,  0,  0,  0,  0,  0,  0]

queenstable = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  5,  5,  5,  5,  5,  0,-10,
0,  0,  5,  5,  5,  5,  0, -5,
-5,  0,  5,  5,  5,  5,  0, -5,
-10,  0,  5,  5,  5,  5,  0,-10,
-10,  0,  0,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]

kingstable = [
20, 30, 10,  0,  0, 10, 30, 20,
20, 20,  0,  0,  0,  0, 20, 20,
-10,-20,-20,-20,-20,-20,-20,-10,
-20,-30,-30,-40,-40,-30,-30,-20,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30]
kingstableendgame = [
-50,-40,-30,-20,-20,-30,-40,-50,
-30,-20,-10,  0,  0,-10,-20,-30,
-30,-10, 20, 30, 30, 20,-10,-30,
-30,-10, 30, 40, 40, 30,-10,-30,
-30,-10, 30, 40, 40, 30,-10,-30,
-30,-10, 20, 30, 30, 20,-10,-30,
-30,-30,  0,  0,  0,  0,-30,-30,
-50,-30,-30,-30,-30,-30,-30,-50]
def init_evaluate_board():
    global boardvalue
    global material
    global whitematerial
    global blackmaterial
    global totalmaterial
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))
    whitematerial = 100*(wp)+320*(wn)+330*(wb)+500*(wr)+900*(wq)
    blackmaterial = 100*(bp)+320*(bn)+330*(bb)+500*(br)+900*(bq) 
    totalmaterial = 100*(wp+bp)+320*(wn+bn)+330*(wb+bb)+500*(wr+br)+900*(wq+bq)
    material = 100*(wp-bp)+320*(wn-bn)+330*(wb-bb)+500*(wr-br)+900*(wq-bq)
    
    pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq= pawnsq + sum([-pawntable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq= sum([bishopstable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq= bishopsq + sum([-bishopstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)]) 
    rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([queenstable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)]) 
    queensq = queensq + sum([-queenstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)]) 
    kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.KING, chess.BLACK)])
    kingsqendgame = sum([kingstableendgame[i] for i in board.pieces(chess.KING, chess.WHITE)]) 
    kingsqendgame = kingsqendgame + sum([-kingstableendgame[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.KING, chess.BLACK)])

    if game == "middlegame":
        boardvalue = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
    if game == "endgame":
        boardvalue = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsqendgame

    return boardvalue
def evaluate_board():
    
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0
    
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))
    
    material = 100*(wp-bp)+320*(wn-bn)+330*(wb-bb)+500*(wr-br)+900*(wq-bq)
    
    pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
    pawnsq= pawnsq + sum([-pawntable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.PAWN, chess.BLACK)])
    knightsq = sum([knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
    knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.KNIGHT, chess.BLACK)])
    bishopsq= sum([bishopstable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
    bishopsq= bishopsq + sum([-bishopstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.BISHOP, chess.BLACK)])
    rooksq = sum([rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)]) 
    rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.ROOK, chess.BLACK)])
    queensq = sum([queenstable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)]) 
    queensq = queensq + sum([-queenstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.QUEEN, chess.BLACK)])
    kingsq = sum([kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)]) 
    kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)] 
                                    for i in board.pieces(chess.KING, chess.BLACK)])
    
    if game == "middlegame":
        eval = material + pawnsq + knightsq + bishopsq+ rooksq+ queensq + kingsq
    if game == "endgame":
        eval = material + pawnsq + knightsq + bishopsq+ rooksq+ queensq + kingsqendgame
    if board.turn:
        return eval
    else:
        return -eval
piecetypes = [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, chess.KING ]
tables = [pawntable, knightstable, bishopstable, rookstable, queenstable, kingstable, kingstableendgame]
piecevalues = [100,320,330,500,900]

def update_eval(mov, side):
    global boardvalue
    
    #update piecequares
    movingpiece = board.piece_type_at(mov.from_square)
    if side:
        boardvalue = boardvalue - tables[movingpiece - 1][mov.from_square]
        #update castling
        if (mov.from_square == chess.E1) and (mov.to_square == chess.G1):
            boardvalue = boardvalue - rookstable[chess.H1]
            boardvalue = boardvalue + rookstable[chess.F1]
        elif (mov.from_square == chess.E1) and (mov.to_square == chess.C1):
            boardvalue = boardvalue - rookstable[chess.A1]
            boardvalue = boardvalue + rookstable[chess.D1]
    else:
        boardvalue = boardvalue + tables[movingpiece - 1][mov.from_square]
        #update castling
        if (mov.from_square == chess.E8) and (mov.to_square == chess.G8):
            boardvalue = boardvalue + rookstable[chess.H8]
            boardvalue = boardvalue - rookstable[chess.F8]
        elif (mov.from_square == chess.E8) and (mov.to_square == chess.C8):
            boardvalue = boardvalue + rookstable[chess.A8]
            boardvalue = boardvalue - rookstable[chess.D8]
        
    if side:
        boardvalue = boardvalue + tables[movingpiece - 1][mov.to_square]
    else:
        boardvalue = boardvalue - tables[movingpiece - 1][mov.to_square]
        
     
    #update material
    if mov.drop != None:
        if side:
            boardvalue = boardvalue + piecevalues[mov.drop-1]
        else:
            boardvalue = boardvalue - piecevalues[mov.drop-1]
            
    #update promotion
    if mov.promotion != None:
        if side:
            boardvalue = boardvalue + piecevalues[mov.promotion-1] - piecevalues[movingpiece-1]
            boardvalue = boardvalue - tables[movingpiece - 1][mov.to_square] \
                + tables[mov.promotion - 1][mov.to_square]
        else:
            boardvalue = boardvalue - piecevalues[mov.promotion-1] + piecevalues[movingpiece-1]
            boardvalue = boardvalue + tables[movingpiece - 1][mov.to_square] \
                - tables[mov.promotion - 1][mov.to_square]
            
            
    return mov

def make_move(mov):
    update_eval(mov, board.turn)
    board.push(mov)
    
    return mov

def unmake_move():
    mov = board.pop()
    update_eval(mov, not board.turn)
    
    return mov

def quiesce( alpha, beta ):
    stand_pat = evaluate_board()
    if( stand_pat >= beta ):
        return beta
    if( alpha < stand_pat ):
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            make_move(move)        
            score = -quiesce( -beta, -alpha )
            unmake_move()

            if( score >= beta ):
                return beta
            if( score > alpha ):
                alpha = score  
    return alpha

def alphabeta( alpha, beta, depthleft ):
    bestscore = -9999
    if( depthleft == 0 ):
        return quiesce( alpha, beta )
    for move in board.legal_moves:
        make_move(move)   
        score = -alphabeta( -beta, -alpha, depthleft - 1 )
        unmake_move()
        if( score >= beta ):
            return score
        if( score > bestscore ):
            bestscore = score
        if( score > alpha ):
            alpha = score   
    return bestscore
        
import chess.polyglot
import chess.gaviota
def selectmove(depth):
    #if material < 1500 :
        #game = "endgame"
    if totalmaterial < 2000:
        game = "endgame"
    try:
        if game == "middlegame":
            move = chess.polyglot.MemoryMappedReader("bookfish.bin").weighted_choice(board).move()
            movehistory.append(move)
        if game == "endgame":
            with chess.gaviota.open_tablebase("data/gaviota") as tablebase:
                result = tablebase.probe_wdl(board)
                #if result == 0:
                    #print ("draw")
                #if result = -2:
                    #print ("resign")
                move = chess.polyglot.MemoryMappedReader("bookfish.bin").weighted_choice(board).move()
                movehistory.append(move)
            
        return move
    except:
        bestMove = chess.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000
        for move in board.legal_moves:
            make_move(move)
            boardValue = -alphabeta(-beta, -alpha, depth-1)
            if boardValue > bestValue:
                bestValue = boardValue;
                bestMove = move
            if( boardValue > alpha ):
                alpha = boardValue
            unmake_move()
        movehistory.append(bestMove)
        return bestMove
def ponder(depthgained):
    if ponder == 1:
        pondermov = selectmove(x-1)
        make_move(pondermov)
        ponderedmove = selectmove(x)
            
        
        
movehistory =[]
board = chess.Board()
boardvalue = init_evaluate_board()
i = 1
x = 5 

if move == 0:
    print (board)
    if color == "black":
        while not board.is_game_over(claim_draw=True):
           ponder = 0
           mov = selectmove(x)
           make_move(mov)
           print (mov)
           SVG(chess.svg.board(board=board,size=400,lastmove=mov))
           print (board)
           playermove = input ("what is your move?")
                        
           board.push_san(playermove)
           print(board)
    if color == "white":
           while not board.is_game_over(claim_draw=True):
               ponder = 1
               playermove = input ("what is your move?")
               board.push_san(playermove)
               print (board)
               ponder = 0
               mov = selectmove(x)
               make_move(mov)
               print (mov)
               SVG(chess.svg.board(board=board,size=400,lastmove=mov))
               print(board)
       

def playstockfish():
    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci("/Program Files/stockfish_20090216_x64")
    print (board)
    if color == "black":
        print ("Lightningwhite")
        while not board.is_game_over(claim_draw=True):
           mov = selectmove(x)
           make_move(mov)
           print (mov)
           

                        
           result = engine.play(board, chess.engine.Limit(time=7))
           board.push(result.move)
    if color == "white":
           print ("Lightningblack")
    
           result = engine.play(board, chess.engine.Limit(time=7))
           board.push(result.move)
           mov = selectmove(x)
           make_move(mov)
           print (mov)
           

    while board.is_game_over(claim_draw=False): 
         print (board)
         board = chess.Board()
         playstockfish()         
           

    

if move == 1011:
    playstockfish()
