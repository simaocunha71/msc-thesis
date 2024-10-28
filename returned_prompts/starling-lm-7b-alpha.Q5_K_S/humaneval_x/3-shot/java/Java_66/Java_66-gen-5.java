        int result = 0;
        for (char c : s.toCharArray()) {
            int ascii_code = (int) c;
            if (ascii_code >= 65 && ascii_code <= 90) {
                result += ascii_code;
            }
        }
        return result;
    }
}

