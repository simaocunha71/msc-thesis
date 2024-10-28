        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            char ac = a.charAt(i);
            char bc = b.charAt(i);
            result.append((char) (ac ^ bc));
        }
        return result.toString();
    }
}

