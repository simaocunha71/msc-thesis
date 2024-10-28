        List<String> ans = new ArrayList<>();

        boolean[] cons = new boolean[26];
        Arrays.fill(cons, true);
        cons['a'] = cons['e'] = cons['i'] = cons['o'] = cons['u'] = false;

        for (int i = 0; i < s.length(); i++) {
            if (cons[s.charAt(i) - 'a']) {
                n--;
                if (n == 0) {
                    StringBuilder sb = new StringBuilder();
                    for (int j = i; j < s.length() && s.charAt(j) != ' '; j++) {
                        if (cons[s.charAt(j) - 'a']) {
                            sb.append(s.charAt(j));
                        } else {
                            ans.add(sb.toString());
                            sb = new StringBuilder();
                        }
                    }
                    if (sb.length() > 0) {
                        ans.add(sb.toString());
                    }
                }
            } else if (s.charAt(i) == ' ') {
                if (n == 0) {
                    StringBuilder sb = new StringBuilder();
                    for (int j = i - 1; j >= 0 && s.charAt(j) != ' '; j--) {
                        if (cons[s.charAt(j) - 'a']) {
                            sb.append(s.charAt(j));
                        } else {
                            ans.add(sb.toString());
                            sb = new StringBuilder();
                        }
                    }
                    if (sb.length() > 0) {
                        ans.add(sb.toString());
                    }
                }
            }
        }
        return ans;
    }
}







































































