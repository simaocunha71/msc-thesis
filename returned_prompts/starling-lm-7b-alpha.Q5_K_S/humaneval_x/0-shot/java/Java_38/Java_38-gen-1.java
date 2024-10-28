        List<String> groups = new ArrayList<>();
        for (int i = 0; i < s.length(); i += 3) {
            groups.add(s.substring(i, Math.min(i + 3, s.length())));
        }
        // cycle elements in each group. Unless group has fewer elements than 3.
        for (int i = 0; i < groups.size(); i++) {
            String group = groups.get(i);
            if (group.length() == 3) {
                groups.set(i, group.substring(1) + group.charAt(0));
                continue A;
            }
        }
        return String.join("", groups);
    }

    /**
    returns the next lexicographical permutation of the string.
    */
    public String nextPermutation(String s) {
        int i = s.length() - 1;
        for (; i > 0; i--) {
            if (s.charAt(i - 1) < s.charAt(i)) {
                break;
            }
        }
        if (i == 0) {
            return "";
        }
        int j = i;
        for (; j < s.length(); j++) {
            if (s.charAt(i - 1) < s.charAt(j)) {
                break;
            }
        }
        char tmp = s.charAt(i - 1);
        s = s.substring(0, i - 1) + s.substring(j, j + 1) + s.substring(i, s.length());
        return s;
    }

    /**
    returns a random permutation of the string.
    */
    public String randomPermutation(String s) {
        Random r = new Random();
        int n = s.length();
        char[] p = s.toCharArray();
        for (int i = 0; i < n; i++) {
            int j = r.nextInt(i + 1);
            char tmp = p[i];
            p[i] = p[j];
