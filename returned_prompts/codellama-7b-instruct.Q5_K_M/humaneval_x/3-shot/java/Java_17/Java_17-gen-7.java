        List<Integer> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();

        for (char c : string.toCharArray()) {
            if (c == 'o') {
                current_string.append(c);
            } else if (c == '|') {
                int current_beat = 0;
                if (current_string.indexOf("o") > -1) {
                    current_beat = 4;
                } else if (current_string.indexOf(".") > -1) {
                    current_beat = 1;
                }
                current_string.setLength(0);
                result.add(current_beat);
            }
        }

        return result;
    }
}

