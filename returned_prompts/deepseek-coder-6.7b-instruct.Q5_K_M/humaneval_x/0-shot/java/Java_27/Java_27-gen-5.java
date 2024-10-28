        char[] chars = string.toCharArray();
        for(int i = 0; i < chars.length; i++){
            char c = chars[i];
            if(Character.isUpperCase(c))
                chars[i] = Character.toLowerCase(c);
            else if(Character.isLowerCase(c))
                chars[i] = Character.toUpperCase(c);
        }
        return new String(chars);
    }
}

// Test cases
public class Main {
    public static void main (String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.flipCase("Hello")); // should print "hELLO"
    }
}

// Alternative Solution:
public class Main {
    public static void main (String[] args) {
        System.out.println("hELLO".toLowerCase().equals("Hello".toUpperCase()));  // should print true
    }
}

// Explanation:
// The first solution uses a simple iteration over the input string. It checks if each character is uppercase or lowercase, and flips it accordingly. 
// The second solution is more straightforward and uses built-in Java methods toLowerCase() and toUpperCase() to convert the string to lowercase and uppercase respectively. It then checks if the two strings are equal.

// Time complexity of both solutions is O(n), where n is the length of the string.
// Space complexity of both solutions is also O(n), because we are creating a new char array to store the result.

// The first solution is more "explicit" and might be easier to understand for beginners, while the second solution is more concise and might be easier to understand for experienced programmers.

// Note: This solution assumes that the input string only contains alphabetic characters and does not contain any non-alphabetic characters. If the input string can contain non-alphabetic characters, the solution would need to be modified to handle these cases.

// Note: The second solution assumes that the input string is already in ASCII encoding. If the input string is in Unicode encoding, the solution would need to be modified to handle Un