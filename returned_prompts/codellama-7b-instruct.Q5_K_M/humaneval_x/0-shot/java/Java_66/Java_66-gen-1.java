import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
     */
    public int digitSum(String s) {
        int sum = 0;
        for (char c: s.toUpperCase().toCharArray()) {
            sum += (int) c;
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(bufferedReader.readLine().trim());
        while (t-- > 0) {
            String s = bufferedReader.readLine().trim();
            Solution obj = new Solution();
            int result = obj.digitSum(s);
            System.out.println(result);
        }
    }
}

