        //Your code here
    }
}

*/

import java.util.*;

public class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<>();
        List<Integer> numbers = new ArrayList<>();

        for (Integer num : arr) {
            if (num >= 1 && num <= 9) {
                numbers.add(num);
            }
        }

        Collections.sort(numbers, Collections.reverseOrder());

        Map<Integer, String> numToName = new HashMap<>();
        numToName.put(1, "One");
        numToName.put(2, "Two");
        numToName.put(3, "Three");
        numToName.put(4, "Four");
        numToName.put(5, "Five");
        numToName.put(6, "Six");
        numToName.put(7, "Seven");
        numToName.put(8, "Eight");
        numToName.put(9, "Nine");

        for (Integer num : numbers) {
            result.add(numToName.get(num));
        }

        return result;
    }
}

//Test Cases:
List<Integer> test1 = Arrays.asList(2, 1, 1, 4, 5, 8, 2, 3); //["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
List<Integer> test2 = Arrays.asList(); //[]
List<Integer> test3 = Arrays.asList(1, -1, 55); //["One"]

Solution solution = new Solution();

System.out.println(solution.byLength(test1));
System.out.println(solution.byLength(test2));
System.out.println(solution.byLength(test3));



































