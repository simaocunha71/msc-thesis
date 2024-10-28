Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public List<String> bf(String planet1, String planet2) {
        String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        List<String> result = new ArrayList<>();
        
        if (!Arrays.asList(planets).contains(planet1) || !Arrays.asList(planets).contains(planet2)) {
            return result;
        }
        
        int index1 = Arrays.asList(planets).indexOf(planet1);
        int index2 = Arrays.asList(planets).indexOf(planet2);
        
        for (int i = index1 + 1; i < index2; i++) {
            result.add(planets[i]);
        }
        
        return result;
    }
}
```
This solution uses an array of planet names and finds the indices of the given planet names. It then iterates over the planets from the index of the first planet to the index of the second planet and adds the planets to the result list. If either of the planet names is not in the list of planet names, it returns an empty list. The result list is then returned. The planets are sorted by proximity to the sun because the array is in order of the planets' distances from the sun. 

Note that this solution assumes that the given planet names are valid (i.e., they are in the list of planet names). If this is not the case, you may want to add error checking to handle invalid planet names. 

Also, this solution returns a list of planet names, not a tuple. If you want to return a tuple, you can modify the solution to return a tuple of the result list and a boolean value indicating whether the result list is empty. 

Here is an example of how you can use this solution:
```java
Solution solution = new Solution();
List<String> result = solution.bf("Jupiter", "Neptune");
System.out.println(result);  // Output: [Saturn, Uranus]
```
This code creates a new instance of the Solution class, calls the bf method with the planet names "Jupiter" and "Neptune", and prints the result list. The output is a list containing the planet names "Saturn" and "Uranus". 

Please note that this solution is case-sensitive, so it will not work correctly if the planet names are not in the correct case