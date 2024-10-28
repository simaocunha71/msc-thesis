        List<String> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            String s = lst.get(i);
            int count = 0;
            for (char c : s.toCharArray()) {
                if ((c - '0') % 2 != 0) {
                    count++;
                }
            }
            result.add(String.format("the number of odd elements %dn the str%dng %d of the %dnput.", count, count, count, count));
        }
        return result;
    }
}

