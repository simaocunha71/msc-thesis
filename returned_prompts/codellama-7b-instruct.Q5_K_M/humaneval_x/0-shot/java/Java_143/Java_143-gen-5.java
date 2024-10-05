import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while (t-- > 0) {
            String sentence = br.readLine().trim();
            String res = "";
            String[] words = sentence.split(" ");
            for (String word : words) {
                if (isPrime(word.length())) {
                    res += word + " ";
                }
            }
            System.out.println(res.trim());
        }
    }

    public static boolean isPrime(int n) {
        // Corner case
        if (n <= 1)
            return false;
        // Check from 2 to n in zero to n-1
        for (int i = 2; i < n; i++)
            if (n % i == 0)
                return false;
        return true;
    }
}
