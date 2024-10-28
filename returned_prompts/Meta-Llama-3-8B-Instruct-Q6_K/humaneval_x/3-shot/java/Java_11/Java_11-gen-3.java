        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            char ca = a.charAt(i);
            char cb = b.charAt(i);
            result.append((char) (ca ^ cb));
        }
        return result.toString();
    }
}

