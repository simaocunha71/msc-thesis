The problem can be solved by comparing each element in the game array with the corresponding element in the guess array. If the guess matches the game, the result is 0. Otherwise, the result is the absolute difference between the guess and the game. 

Here is the Java code for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> compare(List<Integer> game, List<Integer> guess) {
        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < game.size(); i++){
            if(game.get(i) == guess.get(i)){
                result.add(0);
            }else{
                result.add(Math.abs(game.get(i) - guess.get(i)));
            }
        }
        return result;
    }
}
```

This code iterates over the game and guess arrays simultaneously using a for loop. If the current element in the game array matches the current element in the guess array, it adds 0 to the result array. Otherwise, it calculates the absolute difference between the two elements and adds it to the result array. Finally, it returns the result array. 

The compare function can be called with the example inputs as follows:

```java
List<Integer> game = new ArrayList<>(Arrays.asList(1,2,3,4,5,1));
List<Integer> guess = new ArrayList<>(Arrays.asList(1,2,3,4,2,-2));
List<Integer> result = new Solution().compare(game, guess);
System.out.println(result);  // prints [0, 0, 0, 0, 3, 3]

List<Integer> game2 = new ArrayList<>(Arrays.asList(0,5,0,0,0,4));
List<Integer> guess2 = new ArrayList<>(Arrays.asList(4,1,1,0,0,-2));
List<Integer> result2 = new Solution().compare(game2, guess2);
System.out.println(result2);  // prints [4, 4, 1, 0, 0, 6]
``` 