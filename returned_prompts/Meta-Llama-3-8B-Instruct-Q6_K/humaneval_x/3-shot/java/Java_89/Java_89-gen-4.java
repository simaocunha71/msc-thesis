        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String encrypted = "";
        for (char c : s.toLowerCase().toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                int index = alphabet.indexOf(c);
                if (index >= 0) {
                    encrypted += alphabet.charAt((index + 2 * 2) % 26);
                } else {
                    encrypted += c;
                }
            } else {
                encrypted += c;
            }
        }
        return encrypted;
    }
}

