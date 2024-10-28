        String result = String.valueOf(x);
        char[] chars = result.toCharArray();
        shift = shift % chars.length;

        if (shift == 0) return result;
        else if (shift == chars.length) return new String(chars).reverse();

        int first_half = chars.length - shift;
        String first_half_string = new String(Arrays.copyOfRange(chars, chars.length - shift, chars.length));
        String second_half_string = new String(Arrays.copyOfRange(chars, 0, chars.length - shift));

        return second_half_string + first_half_string;
    }
}

