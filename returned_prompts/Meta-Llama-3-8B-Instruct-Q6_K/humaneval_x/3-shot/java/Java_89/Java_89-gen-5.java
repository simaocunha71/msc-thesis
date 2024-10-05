        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        StringBuilder result = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                int index = alphabet.indexOf(Character.toLowerCase(c));
                if (index != -1) {
                    index = (index + alphabet.length() / 2) % alphabet.length();
                    result.append(alphabet.charAt(index));
                } else {
                    result.append(c);
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

