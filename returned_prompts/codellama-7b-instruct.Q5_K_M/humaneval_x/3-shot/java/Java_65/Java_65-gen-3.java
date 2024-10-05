        String result = String.valueOf(x);
        if (shift >= result.length()) {
            result = new StringBuilder(result).reverse().toString();
        } else {
            result = result.substring(shift) + result.substring(0, shift);
        }
        return result;
    }
}

