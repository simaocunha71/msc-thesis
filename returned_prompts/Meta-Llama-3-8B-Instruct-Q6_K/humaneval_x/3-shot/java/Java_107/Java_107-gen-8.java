        int evenCount = 0;
        int oddCount = 0;

        for (int i = 1; i <= n; i++) {
            String str = String.valueOf(i);
            if (isPalindrome(str) && isEven(i)) {
                evenCount++;
            } else if (isPalindrome(str) && !isEven(i)) {
                oddCount++;
            }
        }

        return Arrays.asList(evenCount, oddCount);
    }

    public boolean isPalindrome(String str) {
        int i = 0, j = str.length() - 1;
        while (i < j) {
            if (str.charAt(i) != str.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    public boolean isEven(int num) {
        return num % 2 == 0;
    }
}