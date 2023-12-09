
def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    
    def compare(game,guess):
        result=[]#initializing the array of size equal to total number of games.  
        #if game is less than 5 then the array should contain only one element otherwise it should be an array containing 0 for all the other indices in length.
       if len(game)<5:
           result=game;#array with no other elements except the element that has been compared to get score and guess.
       else:
        #initializing the total score of every game, total guesses of every game and initializing the array as an empty list.
            for i in range(len(guess)):
                if (game[i]==0):
                   result+=[0];#initializing the array with 0 at that particular index that has been compared to get score.
                else:
                    s=abs((score_of_that_particular_index[i]));##comparing scores and guesses
                    tg=(total_guesses_at_tht_particular_index[-1]);#comparing the total guesses with the total of the array that has been initialized above.
                    