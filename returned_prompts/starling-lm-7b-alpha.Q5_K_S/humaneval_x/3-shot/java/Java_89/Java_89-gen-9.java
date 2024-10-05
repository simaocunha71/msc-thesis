        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            char ch = (char) (((c - 'a') + 2 * 2) % 26 + 'a');
            result.append(ch);
        }
        return result.toString();
    }
}

