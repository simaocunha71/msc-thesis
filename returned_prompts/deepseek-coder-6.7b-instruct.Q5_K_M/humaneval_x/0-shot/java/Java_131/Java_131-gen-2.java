        int product = 1;
        boolean hasOdd = false;

        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 != 0) {
                product *= digit;
                hasOdd = true;
            }
            n /= 10;
        }

        return hasOdd ? product : 0;
    }
}

*/

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.digits(1));  // 1
        System.out.println(s.digits(4));  // 0
        System.out.println(s.digits(235));  // 15
    }
}

/*
