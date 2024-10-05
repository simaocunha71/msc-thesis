        List<String> filteredList = new ArrayList<String>();
        for (String str : strings) {
            if (str.contains(substring)) {
                filteredList.add(str);
            }
        }
        return filteredList;
    }
}


A: Here is the correct answer:
import java.util.*;
import java.lang.*;

class Solution  {
    /**
    Filter an input list of strings only for ones that contain given substring
    >>> filterBySubstring(List.of(), "a")
    []
    >>> filterBySubstring(Arrays.asList("abc", "bacd", "cde", "array"), "a")
    ["abc", "bacd", "array"]
      */
    public List<String> filterBySubstring(List<String> strings, String substring)  {
        List<String> filteredList = new ArrayList<>();
        for (String str : strings) {
            if (str.contains(substring)) {
                filteredList.add(str);
            }
        }
        return filteredList;
    }
}


A: In your code, you should not use List.of() to create a list. It is available only from Java 9 onwards. If you are using an older version of Java, you can use Arrays.asList or create a new ArrayList and add elements to it. 
Here is the corrected code:
import java.util.*;

class Solution  {
    public List<String> filterBySubstring(List<String> strings, String substring)  {
        List<String> filteredList = new ArrayList<>();
        for (String str : strings) {
            if (str.contains(substring)) {
                filteredList.add(str);
            }
        }
        return filteredList;
    }
}

Then, you can call this method like this:
Solution solution = new Solution();
List<String> strings = new ArrayList<>(Arrays.asList("abc", "bacd", "cde", "array"));
List<String> filteredStrings = solution.filterBySubstring(strings, "a");
System.out.println(filteredStr