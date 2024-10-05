        List<Integer> result = new ArrayList<>();
        Set<Integer> set = new HashSet<>();
        for(int i=1;i<=n;i++) {
            String str = String.valueOf(i);
            if(str.charAt(0) != str.charAt(str.length()-1)) {
                continue;
            }
            if(str.length()%2 == 0 && isPalindrome(str)) {
                result.add(1);
            } else if(str.length()%2 != 0 && isPalindrome(str)) {
                result.add(0);
            }
        }
        int even = 0;
        int odd = 0;
        for(int i: result) {
            if(i == 0) {
                odd++;
            } else {
                even++;
            }
        }
        result.add(even);
        result.add(odd);
        return result;
    }

    private boolean isPalindrome(String str) {
        int l = 0;
        int r = str.length()-1;
        while(l<r) {
            if(str.charAt(l) != str.charAt(r)) {
                return false;
            }
            l++; r--;
        }
        return true;
    }
}



























































































































































































