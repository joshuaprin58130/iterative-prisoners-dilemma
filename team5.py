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
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.'''
    
    if len(my_history) == 0:
        choice = 'c'    
    elif len(my_history)<=10:
        if their_history[-1] == 'b':
            choice = 'b'
        else:
            choice = 'c'
    else:
        percent = their_history.count('b')/len(their_history)
        if percent >= 0.5:
            choice = 'b'
        else:
            choice = 'c'
            
    return choice
                       