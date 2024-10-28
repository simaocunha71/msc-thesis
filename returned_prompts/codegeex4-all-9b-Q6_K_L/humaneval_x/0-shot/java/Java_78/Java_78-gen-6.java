```java
import java.util.*;
import java.lang.*;

class Solution {
    public int hexKey(String num) {
        Map<Character, Integer> hexToDecimal = new HashMap<>();
        hexToDecimal.put('0', 0);
        hexToDecimal.put('1', 1);
        hexToDecimal.put('2', 2);
        hexToDecimal.put('3', 3);
        hexToDecimal.put('4', 4);
        hexToDecimal.put('5', 5);
        hexToDecimal.put('6', 6);
        hexToDecimal.put('7', 7);
        hexToDecimal.put('8', 8);
        hexToDecimal.put('9', 9);
        hexToDecimal.put('A', 10);
        hexToDecimal.put('B', 11);
        hexToDecimal.put('C', 12);
        hexToDecimal.put('D', 13);
        hexToDecimal.put('E', 14);
        hexToDecimal.put('F', 15);

        Set<Integer> primeNumbers = new HashSet<>();
        primeNumbers.add(2);
        primeNumbers.add(3);
        primeNumbers.add(5);
        primeNumbers.add(7);
        primeNumbers.add(11);
        primeNumbers.add(13);

        int count = 0;
        for (char c : num.toCharArray()) {
            int decimalValue = hexToDecimal.get(c);
            if (primeNumbers.contains(decimalValue)) {
                count++;
            }
        }

        return count;
    }
}
```