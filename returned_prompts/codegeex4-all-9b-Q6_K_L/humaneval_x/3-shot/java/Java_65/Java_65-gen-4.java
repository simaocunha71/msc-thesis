        String result = Integer.toString(x);

        if (shift > result.length()) {
            return new StringBuilder(result).reverse().toString();
        }

        return result.substring(result.length() - shift) + result.substring(0, result.length() - shift);
    }
}

