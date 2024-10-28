        List<String> groups = new ArrayList<>();
        for (int i = 0; i < s.length(); i += 3) {
            groups.add(s.substring(i, Math.min(i + 3, s.length())));
        }

        // reverse elements in each group. Unless group has fewer elements than 3.
        for (int i = groups.size() - 1; i >= 0; i--) {
            if (groups.get(i).length() == 3) {
                groups.set(i, groups.get(i).charAt(2) + groups.get(i).substring(1, 2) + groups.get(i).charAt(0));
            }
        }
        return String.join("", groups);
    }
}

