        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            int index = alphabet.indexOf(c);
            if (index != -1) {
                int new_index = (index + 4) % 26;
                result.append(alphabet.charAt(new_index));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

