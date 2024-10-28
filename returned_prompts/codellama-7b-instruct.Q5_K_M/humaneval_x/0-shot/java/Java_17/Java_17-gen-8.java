        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < string.length(); i++) {
            char c = string.charAt(i);
            if (c == 'o') {
                result.add(4);
                i++;
                continue;
            }
            if (c == '.') {
                result.add(1);
                continue;
            }
            if (c == '|') {
                if (i + 1 < string.length() && string.charAt(i + 1) == '.') {
                    result.add(2);
                } else {
                    result.add(1);
                }
                i++;
                continue;
            }
            throw new IllegalArgumentException();
        }
        return result;
    }
}
