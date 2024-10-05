        int count = 0;
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                    (c == 'y' && i == s.length() - 1)) {
                count++;
            }
        }
        return count;
    }
}
// Test the method
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.vowelsCount("abcde")); // Output: 2
        System.out.println(solution.vowelsCount("ACEDY")); // Output: 3
    }
}
