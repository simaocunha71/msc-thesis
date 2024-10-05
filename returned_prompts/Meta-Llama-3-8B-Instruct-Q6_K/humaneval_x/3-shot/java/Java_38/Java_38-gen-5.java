        List<String> groups = new ArrayList<>();
        for (int i = 0; i < s.length(); i += 3) {
            String group = s.substring(i, Math.min(i + 3, s.length()));
            if (group.length() == 2) {
                groups.add(group + "x");
            } else {
                groups.add(group);
            }
        }
        return String.join("", groups);
    }
}

