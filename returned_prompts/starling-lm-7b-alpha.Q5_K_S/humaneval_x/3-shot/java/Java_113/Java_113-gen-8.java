        List<String> result = new ArrayList<>();
        for (String str : lst) {
            int count = 0;
            for (char c : str.toCharArray()) {
                int num = c - '0';
                if ((num & 1) == 1) count += 1;
            }
            result.add(String.format("the number of odd elements %dn the str%rng %d of the %dnput.", count, str));
        }
        return result;
    }
}

