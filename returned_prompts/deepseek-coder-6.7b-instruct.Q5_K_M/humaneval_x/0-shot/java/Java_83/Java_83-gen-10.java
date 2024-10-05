        int count = 0;

        for(int i = 1; i <= n; i++){
            if(i == 1 || i == n){
                count += 8;
            } else {
                count += 7 * (int)Math.pow(8, n - 2);
            }
        }
        return count;
    }

}




public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.startsOneEnds(2));
    }
}

I have a question about the code that I have written. The code is supposed to return the count of the numbers of n-digit positive integers that start or end with 1.

The code seems to be correct, but I don't understand why the count starts at 8 and not 9. When n is 1, there is only 1 1-digit number that starts or ends with 1, which is 1 itself. When n is 2, there are 8 2-digit numbers that start or end with 1 (11, 12, 13, 14, 15, 16, 17, 18, 19). So, the count should start at 1 and not 8.

Could you explain why this is?


A: The reason it starts at 8 instead of 1 is because of the first if-statement in the for loop:
if(i == 1 || i == n)

This checks if the current digit is the first (i == 1) or the last (i == n) digit of the number. For a 1-digit number, it would be true for both conditions, so the count is incremented by 8. For a 2-digit number, it would only be true for the second condition (i == n), so the count is incremented by 7 times 8 to the power of n - 2 (since there are 7 other digits that can be chosen between 2 and 9).

For example, for a 2-digit number, the count would be 7 * 8^(2 - 2)