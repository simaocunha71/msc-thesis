        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String result = "";
        for (char c : s.toLowerCase().toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                int index = alphabet.indexOf(c);
                result += alphabet.charAt((index + 4 * 2) % 26);
            } else {
                result += c;
            }
        }
        return result;
    }
}

