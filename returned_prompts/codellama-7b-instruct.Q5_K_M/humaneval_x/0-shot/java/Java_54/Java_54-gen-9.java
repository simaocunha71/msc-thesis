        for (int i = 0; i < s0.length(); i++) {
            for (int j = 0; j < s1.length(); j++) {
                if (s0.charAt(i) == s1.charAt(j)) {
                    continue A;
                }
            }
            return false;
        }
        return true;
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.sameChars("eabcdzzzz", "dddzzzzzzzddeddabc"));
        System.out.println(s.sameChars("abcd", "dddddddabc"));
        System.out.println(s.sameChars("dddddddabc", "abcd"));
        System.out.println(s.sameChars("eabcd", "dddddddabc"));
        System.out.println(s.sameChars("abcd", "dddddddabce"));
        System.out.println(s.sameChars("eabcdzzzz", "dddzzzzzzzddddabc"));
    }
}

