    return [abs(guess - game) if guess != game else 0 for guess, game in zip(guess, game)]
#This function takes two lists, guess and game, as input. It uses the zip function to pair up the corresponding elements from the two lists.
#Then it uses a list comprehension to create a new list where each element is the absolute difference between the corresponding elements from the two lists, 
#unless the elements are equal, in which case the element is 0. This new list is then returned. 





# Test the function
print(compare([1,2,3,4,5,1],[1,2,3,4,2,-2])) 
print(compare([0,5,0,0,0,4],[4,1,1,0,0,-2])) 





Output:
[0, 0, 0, 0, 3, 3]
[4, 4, 1, 0, 0, 6]





Explanation:
The function compare takes two lists, guess and game, as input. It uses the zip function to pair up the corresponding elements from the two lists.
Then it uses a list comprehension to create a new list where each element is the absolute difference between the corresponding elements from the two lists, 
unless the elements are equal, in which case the element is 0. This new list is then returned.

The test cases show that the function correctly calculates the difference between the guesses and the actual scores, 
and returns a list of the differences. If the guess is equal to the actual score, the function returns 0 for that index. 





The time complexity of this function is O(n), where n is the length of the input lists, 
because it needs to iterate over the lists once to create the output list. The space complexity is also O(n), 
because it needs to create a new list of the same length as the input lists. 





This function can be used to compare the results of a number of matches, 
where each index in the input lists corresponds to a match, 
and the values in the lists represent the scores and guesses for each match. 
The output list shows how far off each guess was from the actual score. 





This function is useful in many real-world applications, 
such as sports, where teams or players make predictions about the outcomes of matches, 
and the function can be used to compare the predictions with the actual outcomes. 





