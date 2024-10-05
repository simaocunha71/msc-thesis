        List<String> groups = new ArrayList<>();
        for (int i = 0; i < s.length(); i += 3) {
            String group = s.substring(i, Math.min(i + 3, s.length()));
            groups.add(group.substring(1) + group.charAt(0));
        }
        return String.join("", groups);
    }
}

