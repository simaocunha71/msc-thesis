        List<String> groups = new ArrayList<>();
        for (int i = 0; i < s.length(); i += 3) {
            groups.add(s.substring(i, Math.min(i + 3, s.length())));
        }
        // reverse each group.
        Collections.reverse(groups);
        // prepend each group to result.
        StringBuilder result = new StringBuilder();
        for (String group : groups) {
            result.append(group);
        }
        return result.toString();
    }
}

