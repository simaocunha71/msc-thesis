        List<Integer> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();
        for (char c : string.toCharArray()) {
            if (c == '|') {
                if (current_string.length() == 0) {
                    if (c == '|') {
                        result.add(1);
                    } else {
                        result.add(4);
                    }
                } else {
                    if (current_string.charAt(0) == '.') {
                        result.add(1);
                    } else {
                        result.add(2);
                    }
                }
                current_string.setLength(0);
            } else {
                current_string.append(c);
            }
        }
        return result;
    }
}

