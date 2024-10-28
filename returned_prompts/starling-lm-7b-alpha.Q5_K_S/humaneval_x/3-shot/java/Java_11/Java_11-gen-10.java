        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            result.append((char)((int)a.charAt(i) ^ (int)b.charAt(i)));
        }
        return result.toString();
    }
}

