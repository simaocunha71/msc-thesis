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
        StringBuilder result = new StringBuilder();
        for (String group : groups) {
            result.append(group.charAt(1));
            if (group.length() > 1) {
                result.append(group.substring(0, 1) + group.substring(2));
            }
        }
        return result.toString();
    }
}

