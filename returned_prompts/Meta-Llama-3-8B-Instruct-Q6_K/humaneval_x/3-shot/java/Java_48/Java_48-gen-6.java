        String s = text.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        String reverse = new StringBuilder(s).reverse().toString();
        return s.equals(reverse);
    }
}

