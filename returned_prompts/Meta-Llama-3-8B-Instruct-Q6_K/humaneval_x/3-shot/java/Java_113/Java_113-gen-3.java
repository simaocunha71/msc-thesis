        List<String> result = new ArrayList<>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if ((c - '0') % 2 != 0) {
                    count++;
                }
            }
            result.add(String.format("the number of odd elements %dn the str%sng %s of the %snput.", count, s.charAt(0), s, s));
        }
        return result;
    }
}

