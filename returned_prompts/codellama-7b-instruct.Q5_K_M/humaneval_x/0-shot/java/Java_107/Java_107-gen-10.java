        List<Integer> ret = new ArrayList<Integer>();
        for(int i = 1; i <= n; i++) {
            if(isPalindrome(i)) {
                if(isEven(i)) {
                    ret.add(i);
                }
            }
        }
        return ret;
    }

    public boolean isEven(int num) {
        return true;
    }

    public boolean isPalindrome(int num) {
        return true;
    }
}


