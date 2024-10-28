        int evenCount = 0, oddCount = 0;
        for(int i = 1; i <= n; i++) {
            if(isPalindrome(i) && i % 2 == 0) evenCount++;
            else if(isPalindrome(i) && i % 2 != 0) oddCount++;
        }
        return Arrays.asList(evenCount, oddCount);

    }

    public boolean isPalindrome(int num) {
        int temp = num, reverse = 0;
        while(temp > 0) {
            reverse = reverse * 10 + temp % 10;
            temp /= 10;
        }
        return num == reverse;
    }
}