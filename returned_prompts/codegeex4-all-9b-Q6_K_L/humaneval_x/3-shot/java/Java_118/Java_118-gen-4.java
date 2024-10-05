        String vowels = "aeiou";
        StringBuilder result = new StringBuilder();

        for (int i = word.length() - 1; i > 0; i--) {
            char current = word.charAt(i);
            char previous = word.charAt(i - 1);

            if (vowels.indexOf(current) != -1 && vowels.indexOf(previous) == -1) {
                result.append(current);
                break;
            }
        }

        return result.toString();
    }
}

