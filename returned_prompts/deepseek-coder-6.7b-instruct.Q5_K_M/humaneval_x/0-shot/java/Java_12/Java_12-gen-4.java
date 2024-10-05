        if(strings == null || strings.size() == 0){
            return Optional.empty();
        }

        String longest = strings.get(0);
        for (String string : strings) {
            if (string.length() > longest.length()) {
                longest = string;
            }
        }
        return Optional.of(longest);
    }
}


A: You need to import the java.util.Optional class at the beginning of your code, because the return type of the function is an Optional<String>.
Here is the corrected version of your code:
import java.util.*;

class Solution {
    public Optional<String> longest(List<String> strings) {
        if (strings == null || strings.size() == 0) {
            return Optional.empty();
        }

        String longest = strings.get(0);
        for (String string : strings) {
            if (string.length() > longest.length()) {
                longest = string;
            }
        }
        return Optional.of(longest);
    }
}


A: Here is the corrected code.
import java.util.*;

class Solution {
    public Optional<String> longest(List<String> strings) {
        if (strings == null || strings.size() == 0) {
            return Optional.empty();
        }

        String longest = strings.get(0);
        for (String string : strings) {
            if (string.length() > longest.length()) {
                longest = string;
            }
        }
        return Optional.of(longest);
    }
}

You should import java.util.Optional; at the beginning of your code. The return type of the function is an Optional<String>, so you need to use Optional.of() to wrap your String in an Optional object.

A: Here's the corrected code:
import java.util.*;

class Solution {
    public Optional<String> longest(List<String> strings) {
        if (strings == null || strings.size() == 0) {
            return Optional.empty();
        }

        String longest = strings.get(0);
        for (String string :