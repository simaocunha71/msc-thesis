        text = text.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String reverse = new StringBuilder(text).reverse().toString();
        return text.equals(reverse);
    }
}

