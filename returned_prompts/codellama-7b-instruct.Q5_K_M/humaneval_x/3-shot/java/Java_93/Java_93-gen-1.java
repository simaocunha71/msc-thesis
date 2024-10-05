        char[] result = new char[message.length()];
        int i = 0;
        for (char c : message.toCharArray()) {
            if (c >= 'A' && c <= 'Z') {
                result[i] = (char) (c + 2);
            } else if (c >= 'a' && c <= 'z') {
                result[i] = (char) (c - 2);
            } else {
                result[i] = c;
            }
            i += 1;
        }
        return new String(result);
    }
}

