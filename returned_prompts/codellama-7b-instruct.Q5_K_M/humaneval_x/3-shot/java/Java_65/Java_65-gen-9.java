        String result = String.valueOf(x);
        if (result.length() == shift) return new StringBuilder(result).reverse().toString();

        return result.substring(shift) + result.substring(0, shift);
    }
}

