        List<Integer> result = new ArrayList<>();
        int current_count = 0;

        for (char c : string.toCharArray()) {
            if (c == 'o') {
                result.add(4);
                current_count = 4;
            } else if (c == '|') {
                result.add(current_count);
                current_count = 0;
            } else {
                current_count += 1;
            }
        }
        return result;
    }
}

