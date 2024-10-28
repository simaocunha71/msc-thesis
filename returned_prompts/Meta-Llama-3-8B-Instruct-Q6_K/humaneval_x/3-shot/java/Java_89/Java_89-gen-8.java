        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String encrypted = "";
        for (char c : s.toLowerCase().toCharArray()) {
            if (c == ' ') {
                encrypted += ' ';
            } else {
                int index = alphabet.indexOf(c);
                if (index != -1) {
                    encrypted += alphabet.charAt((index + 2 * 2) % 26);
                } else {
                    encrypted += c;
                }
            }
        }
        return encrypted;
    }
}