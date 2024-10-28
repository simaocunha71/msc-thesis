        // Remove spaces and convert to lower case
        text = text.replaceAll("\\s", "").toLowerCase();
        // Check if the string is equal to its reverse
        String reverse = new StringBuilder(text).reverse().toString();
        return text.equals(reverse);
    }
}
