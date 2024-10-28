        List<String> result = new ArrayList<>();
        int len1 = 0;
        int len2 = 0;

        for (String s : lst1) {
            len1 += s.length();
        }

        for (String s : lst2) {
            len2 += s.length();
        }

        if (len1 < len2) {
            for (String s : lst2) {
                if (s.length() < len1) {
                    result.add(s);
                }
            }
        } else if (len1 > len2) {
            for (String s : lst1) {
                if (s.length() < len2) {
                    result.add(s);
                }
            }
        } else {
            for (String s : lst1) {
                result.add(s);
            }
        }

        return result;
    }
} 