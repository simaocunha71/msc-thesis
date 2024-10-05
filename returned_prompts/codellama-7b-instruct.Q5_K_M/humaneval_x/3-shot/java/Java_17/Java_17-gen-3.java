        List<Integer> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();
        int current_depth = 0;

        for (char c : string.toCharArray()) {
            if (c == 'o') {
                current_string.append(c);
                result.add(4);
            } else if (c == '|') {
                current_string.append(c);
                if (current_string.toString().equals("o|")) {
                    result.set(result.size() - 1, 2);
                    current_string.setLength(0);
                } else if (current_string.toString().equals(".|")) {
                    result.set(result.size() - 1, 1);
                    current_string.setLength(0);
                }
            }
        }
        return result;

    }
}

