        String reversed = new StringBuilder(string).reverse().toString();
        for (int i = 0; i < string.length(); i++) {
            if (string.startsWith(reversed.substring(i))) {
                return string + reversed.substring(i);
            }
        }
        return string + reversed;
    }
}

