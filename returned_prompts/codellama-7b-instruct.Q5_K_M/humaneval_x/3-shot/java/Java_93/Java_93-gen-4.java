        String result = "";

        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    if (c == 'Z') {
                        result += (char) (c - 23);
                    } else {
                        result += (char) (c + 2);
                    }
                } else {
                    if (c == 'a') {
                        result += (char) (c + 23);
                    } else {
                        result += (char) (c - 2);
                    }
                }
            } else {
                result += c;
            }
        }
        return result;
    }
}

