        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            int xor = a.charAt(i) ^ b.charAt(i);
            result.append(Integer.toString(xor));
        }
        return result.toString();
    }
}

