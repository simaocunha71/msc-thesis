        List<String> result = new ArrayList<>();

        for (int i = 0; i < string.length(); i++) {
            result.add(string.substring(0, i + 1));
        }

        return result;
    }
}

The solution provided works by iterating over the input string and adding each prefix to the result list. The prefix is obtained by calling substring on the input string with the starting index 0 and ending index i + 1.

The time complexity is O(n^2) because for every character in the string, a substring is created which takes O(n) time. This makes the overall time complexity O(n^2).

The space complexity is O(n) as a new list of size n is created.

In the worst case scenario, the input string consists of n characters, so the number of prefixes will also be n. So, the space requirement is linear.

This solution assumes that the input string is not null. If the input string can be null, then additional null check should be added before the for loop.
*/

public class Main
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Solution solution = new Solution();
        List<String> result = solution.allPrefixes("abc");
        System.out.println(result); // ["a", "ab", "abc"]
    }
}

/*
This code creates an instance of the Solution class and calls the allPrefixes method with the string "abc". The result is printed to the console.
*/
























































































































































