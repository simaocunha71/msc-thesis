        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        StringBuilder result = new StringBuilder();

        for (char c : s.toLowerCase().toCharArray()) {
            if (c == ' ') {
                result.append(c);
            } else {
                int index = alphabet.indexOf(c);
                if (index != -1) {
                    index = (index + 4 * 2) % 26;
                    result.append(alphabet.charAt(index));
                }
            }
        }
        return result.toString();
    }
}

