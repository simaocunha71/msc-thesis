        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String result = "";

        for (char c : s.toLowerCase().toCharArray()) {
            if (c == ' ') {
                result += ' ';
                continue;
            }

            int index = alphabet.indexOf(c);
            if (index == -1) {
                result += c;
                continue;
            }

            index = (index + 2 * 2) % 26;
            result += alphabet.charAt(index);
        }

        return result;
    }
}