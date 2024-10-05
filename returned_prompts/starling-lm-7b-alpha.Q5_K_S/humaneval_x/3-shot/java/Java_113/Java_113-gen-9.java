        List<String> result = new ArrayList<>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if ((c - '0') % 2 != 0) count += 1;
            }
            result.add(String.format("the number of odd elements %dn the str%sng %d of the %dnput.", count, s, count, s.length()));
        }
        return result;
    }
}

