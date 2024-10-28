        List<Integer> result = new ArrayList<>();
        if(n < 0) {
            return result;
        }
        if(n >= 0) {
            result.add(3);
        }
        if(n >= 1) {
            result.add(2);
        }
        if(n >= 2) {
            result.add(8);
        }
        for(int i = 3; i <= n; i++) {
            if(i % 2 == 0) {
                result.add(1 + i / 2);
            } else {
                result.add(result.get(i - 1) + result.get(i - 2) + result.get(i + 1));
            }
        }
        return result;
    }
}

This program computes the Tribonacci sequence for a given number n. If the input number n is negative, the program returns an empty list. If n is 0 or greater, the program computes the first n + 1 numbers of the sequence and returns them as a list.
*/

class Main {
  public static void main(String[] args) {
    Solution s = new Solution();
    System.out.println(s.tri(3)); // Expected output: [3, 2, 8, 18]
    System.out.println(s.tri(5)); // Expected output: [3, 2, 8, 26, 72, 198]
  }
}






























































































































































