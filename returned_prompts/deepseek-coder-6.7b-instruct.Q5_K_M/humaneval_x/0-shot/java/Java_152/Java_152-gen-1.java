    List<Integer> result = new ArrayList<>();
    for(int i = 0; i < game.size(); i++){
        result.add(Math.abs(game.get(i) - guess.get(i)));
    }
    return result;
    }
}

In this question, we are given two lists of scores and guesses. We are asked to find the difference between the scores and guesses, and if they are the same, return 0. If not, return the absolute difference. This is done by using a for loop to iterate over each index of the two lists and calculate the absolute difference. The result is then added to a new list which is returned at the end.
*/

import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> compare(List<Integer> game, List<Integer> guess) {
        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < game.size(); i++){
            result.add(Math.abs(game.get(i) - guess.get(i)));
        }
        return result;
    }
}

public class Main
{
    public static void main(String[] args)
    {
        Solution sol = new Solution();
        List<Integer> game = Arrays.asList(1,2,3,4,5,1);
        List<Integer> guess = Arrays.asList(1,2,3,4,2,-2);
        System.out.println(sol.compare(game, guess));  // [0,0,0,0,3,3]

        game = Arrays.asList(0,5,0,0,0,4);
        guess = Arrays.asList(4,1,1,0,0,-2);
        System.out.println(sol.compare(game, guess));  // [4,4,1,0,0,6]
    }
}

/*
This program first creates a new Solution object. It then creates two lists of scores and guesses, and uses the compare method of the Solution object to get the list of differences. It then prints out the list of differences.
*/