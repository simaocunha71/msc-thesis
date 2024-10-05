    public int search(List<Integer> lst) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : lst) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        for (int num : countMap.keySet()) {
            if (num > 0 && countMap.get(num) >= num) {
                return num;
            }
        }
        return -1;
    } 

R:
The solution iterates over the list, counting the frequency of each number using a HashMap. Then, it iterates over the keys of the HashMap, checking if the number is greater than 0 and its frequency is greater than or equal to the number itself. If such a number is found, it returns the number. If no such number is found, it returns -1. 

The time complexity is O(n), where n is the number of elements in the list, as it needs to iterate over the list twice. The space complexity is O(n), as it uses a HashMap to store the frequency of each number. 

Note that this solution assumes that the input list is non-empty, as specified in the problem statement. If the input list can be empty, the solution should handle this case separately. 

Also, this solution returns the first number that meets the condition, if there are multiple such numbers. If you want to return all such numbers, you can modify the solution to store them in a list and return the list. 





```java
import java.util.*;

class Solution {
    public int search(List<Integer> lst) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : lst) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        for (int num : countMap.keySet()) {
            if (num > 0 && countMap.get(num) >= num) {
                return num;
            }
        }
        return -1;
    }
}
```





```java
import java.util.*;

class Solution {
    public int search(List<Integer> lst) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : lst) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }
        for (int num : countMap.keySet()) {
            if (num > 0 && countMap.get(num) >= num) {
                return num;
            }
