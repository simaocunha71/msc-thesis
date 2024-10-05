        String[] split_by_space = txt.split("\\s");
        if (split_by_space.length > 1) {
            return Arrays.asList(split_by_space);
        }
        String[] split_by_comma = txt.split(",");
        if (split_by_comma.length > 1) {
            return Arrays.asList(split_by_comma);
        }
        int odd_order = 0;
        for (char c : txt.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                if ((c - 'a') % 2 == 1) {
                    odd_order += 1;
                }
            }
        }
        return odd_order;
    }
}

