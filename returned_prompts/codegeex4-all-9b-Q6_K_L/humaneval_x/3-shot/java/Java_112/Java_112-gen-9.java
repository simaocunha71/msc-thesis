        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (c.indexOf(s.charAt(i)) == -1) {
                result.append(s.charAt(i));
            }
        }
        boolean is_palindrome = result.toString().equals(result.reverse().toString());
        return Arrays.asList(result.toString(), is_palindrome);
    }
}

