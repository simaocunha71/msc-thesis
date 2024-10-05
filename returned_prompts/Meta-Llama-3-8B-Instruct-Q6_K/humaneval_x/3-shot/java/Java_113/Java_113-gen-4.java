        List<String> result = new ArrayList<>();
        for (String s : lst) {
            int odd_count = 0;
            for (char c : s.toCharArray()) {
                if ((c - '0') % 2 != 0) {
                    odd_count++;
                }
            }
            result.add(String.format("the number of odd elements %dn the str%dng %d of the %dnput.", odd_count, s.length(), s.length(), s.length()));
        }
        return result;
    }
}

