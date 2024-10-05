        String prefix = string;
        String suffix = new StringBuilder(string).reverse().toString();

        for (int i = 0; i < prefix.length(); i++) {
            if (prefix.startsWith(suffix.substring(i))) {
                return prefix + suffix.substring(i);
            }
        }
        return prefix + suffix;
    }
}

