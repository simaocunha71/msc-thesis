        if(strings.isEmpty()) {
            return Optional.empty();
        }

        String longest = strings.get(0);
        for(String s : strings) {
            if(s.length() > longest.length()) {
                longest = s;
            }
        }

        return Optional.of(longest);
    }
}

The above code will return the longest string from the list. If the list is empty, it will return an empty Optional. If the list contains multiple strings of the same maximum length, it will return the first one.
*/

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        List<String> strings1 = new ArrayList<>();
        System.out.println(solution.longest(strings1)); // Optional.empty

        List<String> strings2 = Arrays.asList("a", "b", "c");
        System.out.println(solution.longest(strings2)); // Optional[a]

        List<String> strings3 = Arrays.asList("a", "bb", "ccc");
        System.out.println(solution.longest(strings3)); // Optional[ccc]
    }
}

The main method runs the above methods with different input lists.

Note: Java 9 and onwards, you can directly use List.of() method to create a list. But it's not available in Java 8. That's why I used new ArrayList<>() and Arrays.asList() methods.
*/















































































































































