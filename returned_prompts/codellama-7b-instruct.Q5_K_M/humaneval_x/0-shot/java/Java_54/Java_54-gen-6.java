        int n = s0.length(), m = s1.length();
        if (n != m) return false;
        int[] count = new int[26];
        for (int i = 0; i < n; i++) {
            count[s0.charAt(i) - 'a']++;
            count[s1.charAt(i) - 'a']--;
        }
        for (int x : count)
            if (x != 0)
                return false;
        return true;
    }

    /**
    Check if two words have the same characters.
    >>> sameChars("eabcdzzzz", "dddzzzzzzzddeddabc")
    true
    >>> sameChars("abcd", "dddddddabc")
    true
    >>> sameChars("dddddddabc", "abcd")
    true
    >>> sameChars("eabcd", "dddddddabc")
    false
    >>> sameChars("abcd", "dddddddabce")
    false
    >>> sameChars("eabcdzzzz", "dddzzzzzzzddddabc")
    false
     */
    public boolean sameChars2(String s0, String s1) {
        char[] chars0 = s0.toCharArray(), chars1 = s1.toCharArray();
        Arrays.sort(chars0);
        Arrays.sort(chars1);
        return Arrays.equals(chars0, chars1);
    }
}
