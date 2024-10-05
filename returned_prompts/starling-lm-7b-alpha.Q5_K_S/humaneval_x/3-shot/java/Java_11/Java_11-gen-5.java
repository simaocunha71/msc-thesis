        StringBuilder result = new StringBuilder();
        int length = a.length();
        for (int i = 0; i < length; i++) {
            int c = a.charAt(i) - '0' ^ b.charAt(i) - '0';
            result.append(c);
        }
        return result.toString();
    }
}

