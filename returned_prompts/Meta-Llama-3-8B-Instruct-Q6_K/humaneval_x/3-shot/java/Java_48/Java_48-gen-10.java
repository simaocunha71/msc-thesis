        text = text.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        return text.equals(new StringBuilder(text).reverse().toString());
    }
}

