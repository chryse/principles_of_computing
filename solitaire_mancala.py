class SolitaireMancala:
    def __init__(self):
        self.board = [0]
        
    def __str__(self):
        copy_board = list(self.board)
        copy_board.reverse()
        return str(copy_board)
    
    def set_board(self, configuration):
        # solve reference issue
        self.board = list(configuration)
    
    def get_num_seeds(self, house_num):
        return self.board[house_num]
    
    def is_legal_move(self, house_num):
        if house_num == 0:
            return False
        elif house_num != self.board[house_num]:
            return False
        elif self.board[house_num] == 0:
            return False
        else:
            return True
    
    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            self.board[house_num] = 0
            for i in range(house_num):
                self.board[i] += 1
        #else:
            #print "illegal move"
    
    # give a legal move 
    def choose_move(self):
        num = 0
        for i in range(1, len(self.board)):
            if self.is_legal_move(i):
                num = i
                break
            else:
                num = 0
        #print "selected index: " + str(num)
        return num         
    
    def is_game_won(self):
        count = 0
        for i in range(1, len(self.board)):
            count += self.board[i]
        return True if count == 0 else False
         
    def plan_moves(self):
        """
        Given a Mancala game, return a list of legal moves
        computed to win the game if possible.
        In computing this sequence, the method repeatedly
        chooses the move whose house is closest to the store
        when given a choice of legal moves. Note that this method
        should not update the current configuration of the game.
        """
        
        #new_board = list(self.board)
        #print new_board
        #if self.is_game_won == False:
            #print "work"
            #for 
            #print self.board
        #return new_board
        for dummy_house in range(len(self.board)):
            dummy_mancala = SolitaireMancala()
            dummy_mancala.set_board(self.board)
            move_list = []
        
            while dummy_mancala.choose_move() != 0:
                move_list.append(dummy_mancala.choose_move())
                dummy_mancala.apply_move(move_list[-1])
        
            return move_list
        
    
    
# test module
import poc_mancala_testsuite
poc_mancala_testsuite.run_test(SolitaireMancala)

#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala())
#poc_mancala_gui.MancalaGUI(SolitaireMancala())

# my own import
#import user34_V4IZ4ziiPC_3 as MancalaGUI
#MancalaGUI.run_gui(SolitaireMancala())

#import user34_V4IZ4ziiPC_3
#user34_V4IZ4ziiPC_3.run_gui(SolitaireMancala())

print "test"