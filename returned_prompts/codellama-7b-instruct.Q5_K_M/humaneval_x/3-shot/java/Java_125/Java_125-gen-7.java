        String[] words = txt.split("\\s+");
        if (words.length > 0) {
            return Arrays.asList(words);
        }

        words = txt.split(",");
        if (words.length > 0) {
            return Arrays.asList(words);
        }

        int count = 0;
        for (char c : txt.toCharArray()) {
            if (Character.isLowerCase(c) && Character.getNumericValue(c) % 2 != 0) {
                count++;
            }
        }
        return count;
    }
}

