        String vowels = "aeiou";
        char[] chars = text.toCharArray();
        StringBuilder result = new StringBuilder();
        for (char c : chars) {
            if (!vowels.contains(String.valueOf(c))) result.append(c);
        }
        return result.toString();
    }
}

