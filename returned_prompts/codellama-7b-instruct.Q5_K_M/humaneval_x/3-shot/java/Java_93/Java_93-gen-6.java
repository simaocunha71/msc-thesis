        char[] encoded = new char[message.length()];

        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);

            if (c >= 'A' && c <= 'Z') {
                if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                    encoded[i] = (char) (c + 2);
                } else {
                    encoded[i] = (char) (c - 2);
                }
            } else {
                if (c >= 'a' && c <= 'z') {
                    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                        encoded[i] = (char) (c + 2);
                    } else {
                        encoded[i] = (char) (c - 2);
                    }
                } else {
                    encoded[i] = c;
                }
            }
        }
        return String.valueOf(encoded);
    }
}

