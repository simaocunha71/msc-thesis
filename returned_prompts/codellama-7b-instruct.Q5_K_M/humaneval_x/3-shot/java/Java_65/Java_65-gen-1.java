        String result = String.valueOf(x);
        int length = result.length();
        if (shift >= length) {
            result = result.chars()
                    .mapToObj(c -> (char) c)
                    .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                    .toString();
        } else {
            result = result.substring(shift) + result.substring(0, shift);
        }
        return result;
    }
}

