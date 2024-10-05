        List<String> groups = new ArrayList<>();
        StringBuilder current_group = new StringBuilder();
        for (char c : s.toCharArray()) {
            current_group.append(c);
            if (current_group.length() == 3) {
                groups.add(current_group.toString());
                current_group.setLength(0);
            }
        }
        if (!current_group.toString().isEmpty()) {
            groups.add(current_group.toString());
        }
        StringBuilder decoded_string = new StringBuilder();
        for (String group : groups) {
            decoded_string.append(group.charAt(1));
            if (group.length() == 3) {
                decoded_string.append(group.charAt(0));
            }
        }
        return decoded_string.toString();
    }
}

