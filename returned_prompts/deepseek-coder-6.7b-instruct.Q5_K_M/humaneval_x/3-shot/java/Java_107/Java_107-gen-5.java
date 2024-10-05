        int evenCount = 0, oddCount = 0;
        for(int i = 1; i <= n; i++){
            if(isPalindrome(i)){
                if(i % 2 == 0) evenCount++;
                else oddCount++;
            }
        }
        return Arrays.asList(evenCount, oddCount);
    }
    
    public boolean isPalindrome(int num){
        String str = String.valueOf(num);
        int start = 0, end = str.length() - 1;
        while(start < end){
            if(str.charAt(start) != str.charAt(end)) return false;
            start++;
            end--;
        }
        return true;
    }
}

