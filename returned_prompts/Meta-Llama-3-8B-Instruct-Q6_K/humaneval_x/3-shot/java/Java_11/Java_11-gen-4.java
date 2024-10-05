        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            result.append((a.charAt(i) ^ b.charAt(i)) == 1 ? "1" : "0");
        }
        return result.toString();
    }
}

