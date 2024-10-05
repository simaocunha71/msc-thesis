        String result = "";
        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);
            if (Character.isLowerCase(c)) {
                result += (char) (c + 2);
            } else if (Character.isUpperCase(c)) {
                result += (char) (c - 2);
            } else {
                result += c;
            }
        }
        return result;
    }
}

