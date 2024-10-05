        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            result.append((char) (c + 1));
        }
        return result.toString();
    }
}

