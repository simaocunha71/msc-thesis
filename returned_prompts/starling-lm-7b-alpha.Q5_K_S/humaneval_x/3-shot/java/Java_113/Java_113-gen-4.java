        List<String> result = new ArrayList<>();
        for (String number : lst) {
            int odd_count = 0;
            for (char c : number.toCharArray()) {
                int d = c - '0';
                if ((d & 1) == 1) odd_count += 1;
            }
            result.add(String.format("the number of odd elements %dn the str%dng %d of the %dnput.", odd_count,
                                     odd_count, odd_count, odd_count));
        }
        return result;
    }
}

