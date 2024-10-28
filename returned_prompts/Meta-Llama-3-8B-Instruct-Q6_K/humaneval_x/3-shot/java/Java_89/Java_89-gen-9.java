        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String result = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'z') {
                int index = alphabet.indexOf(c);
                if (index != -1) {
                    index = (index + 4 * 2) % 26;
                    result += alphabet.charAt(index);
                } else {
                    result += c;
                }
            } else {
                result += c;
            }
        }
        return result;
    }
}

