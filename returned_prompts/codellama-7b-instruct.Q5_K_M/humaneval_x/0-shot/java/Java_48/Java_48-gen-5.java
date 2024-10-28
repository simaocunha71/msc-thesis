        //convert to lower case
        text = text.toLowerCase();

        //remove all non-alphanumeric characters
        text = text.replaceAll("[^a-z0-9]", "");

        //check for empty string
        if (text.length() == 0) {
            return true;
        }

        //check for palindrome
        for (int i = 0; i < text.length() / 2; i++) {
            if (text.charAt(i) != text.charAt(text.length() - 1 - i)) {
                return false;
            }
        }

        return true;
    }
}

