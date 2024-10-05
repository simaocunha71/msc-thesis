        StringBuilder result = new StringBuilder();
        boolean is_letter = false;

        for (char c : s.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                result.append((char) (c - 'a' + 'A'));
                is_letter = true;
            } else if (c >= 'A' && c <= 'Z') {
                result.append((char) (c - 'A' + 'a'));
                is_letter = true;
            } else {
                result.append(c);
            }
        }
        if (!is_letter) {
            return new StringBuilder(s).reverse().toString();
        } else {
            return result.reverse().toString();
        }
    }
}

