        String result = "";
        String lowercase = s.toLowerCase();
        for (char c : lowercase.toCharArray()) {
            int char_int = (int) c;
            if (c >= 'a' && c <= 'z') {
                char_int = (char_int + 2 * 2) % 26;
            }
            result += (char) char_int;
        }
        return result;
    }
}

