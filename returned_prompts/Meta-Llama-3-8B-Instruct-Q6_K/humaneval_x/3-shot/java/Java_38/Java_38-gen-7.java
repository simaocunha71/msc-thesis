        List<String> groups = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();
        for (char c : s.toCharArray()) {
            current_string.append(c);
            if (current_string.length() == 3) {
                groups.add(current_string.toString());
                current_string.setLength(0);
            }
        }
        // reverse order of elements in each group. Unless group has fewer elements than 3.
        for (int i = 0; i < groups.size(); i++) {
            if (groups.get(i).length() == 3) {
                groups.set(i, groups.get(i).charAt(2) + groups.get(i).substring(1));
            } else {
                groups.set(i, groups.get(i) + groups.get(i));
            }
        }
        return String.join("", groups);
    }
}

