        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String encrypted_s = "";

        for (char c : s.toCharArray()) {
            int index = alphabet.indexOf(c);
            if (index == -1) {
                encrypted_s += c;
            } else {
                encrypted_s += alphabet.charAt((index + 4) % 26);
            }
        }
        return encrypted_s;
    }
}

