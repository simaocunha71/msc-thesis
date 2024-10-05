        List<String> result = new ArrayList<>();
        int index = 0;

        while (index < s.length()) {
            int current_length = 0;
            int current_index = index;

            while (index < s.length() && s.charAt(index) != ' ') {
                current_length += 1;
                index += 1;
            }

            if (current_length == n) {
                result.add(s.substring(current_index, current_index + current_length));
            }
            index += 1;
        }
        return result;
    }
}

