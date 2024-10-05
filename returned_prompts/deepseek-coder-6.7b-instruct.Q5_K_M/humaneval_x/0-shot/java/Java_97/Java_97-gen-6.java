        // Write your code here.
        int lastDigitA = Math.abs(a) % 10;
        int lastDigitB = Math.abs(b) % 10;
        return lastDigitA * lastDigitB;
    }
}

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        System.out.println(sol.multiply(148, 4