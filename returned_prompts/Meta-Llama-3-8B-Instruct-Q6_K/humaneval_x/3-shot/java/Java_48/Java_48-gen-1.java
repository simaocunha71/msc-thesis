        String clean_text = text.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        return clean_text.equals(new StringBuilder(clean_text).reverse().toString());
    }
}

