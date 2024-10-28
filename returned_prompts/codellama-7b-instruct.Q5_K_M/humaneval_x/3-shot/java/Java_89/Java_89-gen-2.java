        String result = "";
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    char new_c = (char) (((c - 'A') + 2) % 26 + 'A');
                    result += new_c;
                } else {
                    char new_c = (char) (((c - 'a') + 2) % 26 + 'a');
                    result += new_c;
                }
            } else {
                result += c;
            }
        }
        return result;
    }
}

