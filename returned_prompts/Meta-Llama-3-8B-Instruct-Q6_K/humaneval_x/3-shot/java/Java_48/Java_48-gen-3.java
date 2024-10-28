        text = text.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String reversed = new StringBuilder(text).reverse().toString();
        return text.equals(reversed);
    }
}

