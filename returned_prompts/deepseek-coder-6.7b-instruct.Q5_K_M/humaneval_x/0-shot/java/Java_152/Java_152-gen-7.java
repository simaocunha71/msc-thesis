        List<Integer> result = new ArrayList<>();

        for(int i = 0; i < game.size(); i++){
            result.add(Math.abs(game.get(i) - guess.get(i)));
        }

        return result;
    }
}

```

## Answer:
```java
import java.util.*;
import java.lang.*;

class Solution  {
    public List<Integer> compare(List<Integer> game, List<Integer> guess)  {
        List<Integer> result = new ArrayList<>();

        for(int i = 0; i < game.size(); i++){
            result.add(Math.abs(game.get(i) - guess.get(i)));
        }

        return result;
    }
}
```

## Explanation:
The `compare` method takes two lists of integers, `game` and `guess`. It iterates over the `game` list and for each element at index `i`, it calculates the absolute difference between the `i-th` element of `game` and `guess`. This difference is then added to the `result` list. Finally, it returns the `result` list.

## Test Case:
```java
public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.compare(Arrays.asList(1,2,3,4,5,1), Arrays.asList(1,2,3,4,2,-2)));  // Expected output: [0, 0, 0, 0, 3, 3]
    System.out.println(solution.compare(Arrays.asList(0,5,0,0,0,4), Arrays.asList(4,1,1,0,0,-2)));  // Expected output: [4, 4, 1, 0, 0, 6]
}
```

## Output:
```
[0, 0, 0, 0, 3, 3]
[4, 4, 1, 0, 0, 6]
```
