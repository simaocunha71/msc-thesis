        List<String> groups = new ArrayList<>();
        StringBuilder group = new StringBuilder();
        for (char c : s.toCharArray()) {
            group.append(c);
            if (group.length() == 3) {
                groups.add(group.toString());
                group.setLength(0);
            }
        }
        if (!group.toString().isEmpty()) {
            groups.add(group.toString());
        }
        return String.join("", groups);
    }
}