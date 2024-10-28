        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String encrypted_alphabet = alphabet.substring(4) + alphabet.substring(0, 4);
        StringBuilder encrypted_string = new StringBuilder();
        for (char c : s.toCharArray()) {
            int index = alphabet.indexOf(c);
            if (index == -1) {
                encrypted_string.append(c);
            } else {
                encrypted_string.append(encrypted_alphabet.charAt(index));
            }
        }
        return encrypted_string.toString();
    }
}

