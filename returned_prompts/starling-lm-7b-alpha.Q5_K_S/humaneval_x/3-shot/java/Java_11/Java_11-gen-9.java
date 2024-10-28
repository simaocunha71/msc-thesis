        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            result.append((char) (a.charAt(i) ^ b.charAt(i)));
        }
        return result.toString();
    }
}


