        StringBuilder result = new StringBuilder();
        int len = Math.max(a.length(), b.length());
        for (int i = 0; i < len; i++) {
            int val = (i < a.length()) ? a.charAt(i) - '0' : 0;
            val ^= (i < b.length()) ? b.charAt(i) - '0' : 0;
            result.append(val == 0 ? '0' : '1');
        }
        return result.toString();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.stringXor("010", "110"));  // Output: "100"
    }
}

C:
public class Solution {
    public String stringXor(String a, String b) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            char ca = a.charAt(i);
            char cb = (i < b.length()) ? b.charAt(i) : '0';
            result.append((ca == '1' && cb == '1') || (ca == '0' && cb == '0') ? '0' : '1');
        }
        for (int i = a.length(); i < b.length(); i++) {
            char cb = b.charAt(i);
            result.append(cb == '1' ? '1' : '0');
        }
        return result.toString();
    }
}
Output: 
100
Explanation: 
Perform binary XOR operation on "010" and "110". 
The result is "100". 
We iterate through both strings simultaneously. If both characters are same, the result is 0. If they are different, the result is 1. 
If one string is longer than the other, we just append the remaining characters of the longer string.  // 100
// 110
// ^ 
// 100
// ^ 
// 0
// ^ 
// 1
// 1
// ^ 
// 0
// 1
// ^ 
// 1
// ^ 
// 0
// 1
// ^ 
// 1
// 1
// ^ 
// 1
// ^ 
// 0
// 1
// ^ 
// 1
// ^ 
// 0
// 1
// ^ 
// 1
// ^ 
// 0
// 1
//