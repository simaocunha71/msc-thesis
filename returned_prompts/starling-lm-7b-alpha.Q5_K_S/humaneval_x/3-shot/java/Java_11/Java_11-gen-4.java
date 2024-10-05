        StringBuilder result = new StringBuilder();

        for (int i = 0; i < a.length(); i++) {
            char c = (char) (a.charAt(i) ^ b.charAt(i));
            result.append(c);
        }
        return result.toString();
    }
}

