        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isUpperCase(c)) {
                result.append((char) ('A' + (c - 'A' + 10) % 26));
            } else {
                result.append((char) ('a' + (c - 'a' + 10) % 26));
            }
        }
        return result.toString();
     }
}

