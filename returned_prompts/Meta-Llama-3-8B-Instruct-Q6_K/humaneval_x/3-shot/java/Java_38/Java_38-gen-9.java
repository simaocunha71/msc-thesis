        List<String> groups = new ArrayList<>();
        StringBuilder current_group = new StringBuilder();

        for (char c : s.toCharArray()) {
            current_group.append(c);

            if (current_group.length() == 3) {
                groups.add(current_group.toString());
                current_group.setLength(0);
            }
        }

        if (current_group.length() > 0) {
            groups.add(current_group.toString());
        }

        StringBuilder result = new StringBuilder();

        for (String group : groups) {
            result.append(group.charAt(1));
            result.append(group.charAt(2));
            result.append(group.charAt(0));
        }

        return result.toString();
    }
}

