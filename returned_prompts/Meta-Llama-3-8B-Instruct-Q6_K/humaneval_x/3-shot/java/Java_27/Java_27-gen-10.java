        StringBuilder result = new StringBuilder();
        for (char c : string.toCharArray()) {
            result.append(c >= 'a' && c <= 'z' ? (char) (c - 32) : (char) (c + 32));
        }
        return result.toString();
    }
}

