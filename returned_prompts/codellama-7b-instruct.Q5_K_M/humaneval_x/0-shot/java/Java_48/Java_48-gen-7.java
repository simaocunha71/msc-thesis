        int length = text.length();
        int mid = length / 2;
        int i = 0;
        int j = length - 1;

        while (i < mid) {
            char c1 = text.charAt(i);
            char c2 = text.charAt(j);
            if (c1 != c2) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isPalindrome(""));
        System.out.println(sol.isPalindrome("aba"));
        System.out.println(sol.isPalindrome("aaaaa"));
        System.out.println(sol.isPalindrome("zbcd"));
    }
}

