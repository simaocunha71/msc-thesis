        List<Integer> list = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            String s = String.valueOf(i);
            if (isPalindrome(s)) {
                if (isEven(s)) {
                    list.add(Integer.valueOf(s));
                }
            }
        }

        return list;
    }

    private boolean isEven(String s) {
        return s.length() % 2 == 0;
    }

    private boolean isPalindrome(String s) {
        int n = s.length();
        for (int i = 0; i < n / 2; i++) {
            if (s.charAt(i) != s.charAt(n - i - 1)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int n = 100;
        List<Integer> list = new Solution().evenOddPalindrome(n);
        System.out.println(list.size());
    }
}

