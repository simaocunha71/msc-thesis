        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            int bitA = a.charAt(i) - '0';
            int bitB = b.charAt(i) - '0';
            result.append(bitA ^ bitB);
        }
        return result.toString();
    }
}

