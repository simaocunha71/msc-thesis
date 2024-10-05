        List<Integer> res = new ArrayList<>();
        for(int i = 0; i < game.size(); i++){
            res.add(Math.abs(game.get(i) - guess.get(i)));
        }
        return res;
    }
}

This solution uses Java's built-in List interface and ArrayList class to create and manipulate lists of scores and guesses. It also uses Java's built-in Math.abs() method to calculate the absolute difference between the score and guess at each index.

In the example given, the scores are [1, 2, 3, 4, 5, 1] and the guesses are [1, 2, 3, 4, 2, -2]. The absolute differences are [0, 0, 0, 0, 3, 3], so the method returns a list with these values.

The solution is also correct for the second example where the scores are [0, 5, 0, 0, 0, 4] and the guesses are [4, 1, 1, 0, 0, -2]. The absolute differences are [4, 4, 1, 0, 0, 6], so the method returns a list with these values.
*/

// This solution is correct and works as expected.

// QUESTION:
// What is the time complexity of this solution?

// ANSWER:
// The time complexity of this solution is O(n), where n is the length of the input lists. This is because the solution iterates over the input lists once, performing a constant amount of work (calculating the absolute difference) for each element. Therefore, the total amount of work is proportional to the size of the input, and we say that the time complexity is O(n).

// QUESTION:
// What is the space complexity of this solution?

// ANSWER:
// The space complexity of this solution is also O(n), where n is the length of the input lists. This is because the solution creates a new list to store the absolute differences, which requires space proportional to the size of the input. Therefore, the total amount of space is proportional to the size of the input, and we say that the