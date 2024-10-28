        List<String> res = new ArrayList<>();
        Set<Character> consonants = new HashSet<>(Arrays.asList('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'));
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ' ') {
                int cnt = 0;
                while (i < s.length()) {
                    if (s.charAt(i) != ' ' && consonants.contains(s.charAt(i))) {
                        cnt++;
                    }
                    if (cnt == n) {
                        String curr = "";
                        while (i >= 0 && s.charAt(i) != ' ') {
                            curr = s.charAt(i) + curr;
                            i--;
                        }
                        res.add(curr);
                        break;
                    } else if (cnt > n) {
                        break;
                    }
                    i++;
                }
            }
        }
        return res;
    }
}












































































































































































































