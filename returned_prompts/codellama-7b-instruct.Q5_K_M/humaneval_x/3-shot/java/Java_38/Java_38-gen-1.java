        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i += 3) {
            String group = s.substring(i, Math.min(i + 3, s.length()));
            result.append(group.charAt(1) + group.substring(2));
            if (i + 3 < s.length()) result.append(s.charAt(i + 3));
        }
        return result.toString();
    }
}

