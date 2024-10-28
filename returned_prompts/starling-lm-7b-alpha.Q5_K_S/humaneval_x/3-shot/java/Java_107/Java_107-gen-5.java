        int even = 0;
        int odd = 0;

        for (int i = 1; i <= n; i++) {
            int reversed = reverse(i);
            if (reversed == i && (i % 2 == 0)) {
                even += 1;
            } else if (reversed == i && (i % 2 != 0)) {
                odd += 1;
            }
        }
        List<Integer> result = new ArrayList<>();
        result.add(even);
        result.add(odd);
        return result;
    }

    private int reverse(int i) {
        int reversed = 0;
        while (i > 0) {
            int remainder = i % 10;
            reversed = reversed * 10 + remainder;
            i /= 10;
        }
        return reversed;
    }
}


public class CodeChallenge {

    public static void main(String[] args) {
        Solution solution = new Solution();
        solution.evenOddPalindrome(3);
    }
}

```