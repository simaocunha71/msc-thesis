        List<String> result = new ArrayList<>();
        boolean is_consonant;
        for (char c : s.toCharArray()) {
            is_consonant = Character.isLetter(c) && !Character.isLowerCase(c);
            if (is_consonant && n == 0) {
                result.add(String.valueOf(c));
                n -= 1;
            } else if (is_consonant) {
                result.add(String.valueOf(c));
                n -= 1;
            }
        }
        return result;
    }
}

