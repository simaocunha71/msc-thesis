        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            int num = (ch - 'a') % 26;
            sb.append((char) (num + 'a'));
        }
        return sb.toString();
    }

    /**
    returns encoded string by shifting every character by 1 in the alphabet.
     */
    public String encodeShift3(String s) {
        StringBuilder sb = new StringBuilder();