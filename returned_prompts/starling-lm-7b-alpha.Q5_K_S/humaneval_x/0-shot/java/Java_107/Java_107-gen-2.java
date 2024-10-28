        List<Integer> res = new ArrayList<>();
        int odd = 0;
        int even = 0;
        for(int i = 1; i <= n; i++) {
            String s = i + "";
            if(isPalindrome(s)) {
                if(i % 2 == 0) even++;
                else odd++;
            }
        }
        res.add(even);
        res.add(odd);
        return res;
    }

    private boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while(i < j) {
            if(s.charAt(i) != s.charAt(j)) return false;
            i++; j--;
        }
        return true;
    }
}










































```