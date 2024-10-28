        String encoded = "";
        String vowels = "aeiouAEIOU";

        for (char c : message.toCharArray()) {
            if (vowels.contains(Character.toString(c))) {
                encoded += (char) (c + 2);
            } else if (Character.isLowerCase(c)) {
                encoded += Character.toUpperCase(c);
            } else if (Character.isUpperCase(c)) {
                encoded += Character.toLowerCase(c);
            }
        }
        return encoded;
    }
}

