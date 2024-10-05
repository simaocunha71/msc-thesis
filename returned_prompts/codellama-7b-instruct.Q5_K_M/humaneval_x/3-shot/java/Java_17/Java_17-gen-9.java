        List<Integer> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();
        for (char c : string.toCharArray()) {
            if (c == 'o') {
                if (current_string.length() > 0) {
                    result.add(Integer.parseInt(current_string.toString()));
                    current_string.setLength(0);
                }
                result.add(4);
            } else if (c == '|') {
                if (current_string.length() > 0) {
                    result.add(Integer.parseInt(current_string.toString()));
                    current_string.setLength(0);
                }
                result.add(2);
            } else if (c == '.') {
                if (current_string.length() > 0) {
                    result.add(Integer.parseInt(current_string.toString()));
                    current_string.setLength(0);
                }
                result.add(1);
            } else {
                current_string.append(c);
            }
        }
        if (current_string.length() > 0) {
            result.add(Integer.parseInt(current_string.toString()));
        }
        return result;

    }
}

