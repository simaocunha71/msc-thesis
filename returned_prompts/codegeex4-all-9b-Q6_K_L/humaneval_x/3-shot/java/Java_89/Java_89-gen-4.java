        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String rotatedAlphabet = alphabet.substring(4) + alphabet.substring(0, 4);
        StringBuilder encrypted = new StringBuilder();

        for (char c : s.toCharArray()) {
            int index = alphabet.indexOf(Character.toLowerCase(c));
            if (index != -1) {
                char encryptedChar = rotatedAlphabet.charAt(index);
                encrypted.append(Character.isLowerCase(c) ? encryptedChar : Character.toUpperCase(encryptedChar));
            } else {
                encrypted.append(c);
            }
        }

        return encrypted.toString();
    }
}

