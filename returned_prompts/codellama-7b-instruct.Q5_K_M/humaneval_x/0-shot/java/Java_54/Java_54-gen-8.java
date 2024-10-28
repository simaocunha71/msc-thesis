        if (s0.length() != s1.length()) return false;
        Set<Character> s0Set = new HashSet<Character>();
        for (char c : s0.toCharArray()) s0Set.add(c);
        for (char c : s1.toCharArray()) {
            if (s0Set.contains(c)) continue;
            else return false;
        }
        return true;
    }
    public static void main(String[] args) {
        Solution test = new Solution();
        String[] tests = {
            "abcd", "dddddddabc",
            "abcd", "dddddddabce",
            "eabcdzzzz", "dddzzzzzzzddeddabc",
            "eabcdzzzz", "dddzzzzzzzddddabc",
        };
        for (int i = 0; i < tests.length; i += 2) {
            System.out.println(String.format(">>> sameChars(\"%s\", \"%s\")", tests[i], tests[i + 1]));
            System.out.println(test.sameChars(tests[i], tests[i + 1]));
        }
    }
}
