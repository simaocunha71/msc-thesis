        int evenCount = 0;
        int oddCount = 0;

        for(int i = 1; i <= n; i++) {
            if(isPalindrome(i)) {
                if(i % 2 == 0) evenCount++;
                else oddCount++;
            }
        }

        return Arrays.asList(evenCount, oddCount);
    }

    private boolean isPalindrome(int n) {
        String str = String.valueOf(n);
        int i = 0, j = str.length() - 1;

        while(i < j) {
            if(str.charAt(i) != str.charAt(j)) return false;
            i++;
            j--;
        }

        return true;
    }
}

