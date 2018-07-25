####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'OJ' # Only 10 chars displayed.
strategy_name = 'Collude, but retaliate, then let history decide'
strategy_description = 'For the first 10 rounds, collude unless betrayed. After 10 rounds, betray if opponent betray rate is greater than 50%.'
    
def move(my_history, their_history, my_score, their_score):
    '''The thought process behind this strategy is that collusion is the optimal strategy IF your opponent is willing to collude. The code here
    is designed to be generous at the start, by colluding with no prior knowledge. For the rest of the first 10 turns, the algorithm will default to
    colluding UNLESS betrayed in the previous round. After 10 rounds are complete, the algorithm examines the history of the opponent. The algorithm
    will collude if the opponent has a history of colluding (50% or greater collusion rate), but will betray otherwise.'''
    
    if len(my_history) == 0:
        choice = 'c'    
    elif len(my_history)<=10:
        if their_history[-1] == 'b':
            choice = 'b'
        else:
            choice = 'c'
    else:
        betray_rate = their_history.count('b')/len(their_history)
        if betray_rate >= 0.5:
            choice = 'b'
        else:
            choice = 'c'
            
    return choice
                       