        List<String> res = new ArrayList<>();
        boolean[] is_vowel = new boolean[26];
        Arrays.fill(is_vowel, true);
        is_vowel['a'-'a'] = false;
        is_vowel['e'-'a'] = false;
        is_vowel['i'-'a'] = false;
        is_vowel['o'-'a'] = false;
        is_vowel['u'-'a'] = false;

        StringBuilder sb = new StringBuilder();
        for (char c: s.toCharArray()) {
            if (c == ' ') {
                int count = sb.length();
                if (count == n && is_vowel(sb.toString())) {
                    res.add(sb.toString());
                } else if (count > n) {
                    continue A;
                }
                sb.setLength(0);
            } else {
                sb.append(c);
            }
        }
        if (sb.length() == n && is_vowel(sb.toString())) {
            res.add(sb.toString());
        }
        return res;
    }

    private boolean is_vowel(String s) {
        for (char c: s.toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                return false;
            }
        }
        return true;
    }
}




































































































































