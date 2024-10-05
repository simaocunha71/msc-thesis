        List<String> groups = new ArrayList<>();
        for (int i = 0; i < s.length(); i += 3) {
            groups.add(s.substring(i, Math.min(i + 3, s.length())));
        }
        // reverse each group and concatenate.
        for (int i = 0; i < groups.size(); i++) {
            groups.set(i, new StringBuilder(groups.get(i)).reverse().toString());
        }
        return String.join("", groups);
    }
}

