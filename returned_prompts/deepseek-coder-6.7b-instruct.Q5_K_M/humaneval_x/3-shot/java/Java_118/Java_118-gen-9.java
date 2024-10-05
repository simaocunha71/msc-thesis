        String vowels = "AEIOUaeiou";
        StringBuilder result = new StringBuilder();

        for (int i = word.length() - 2; i > 0; i--) {
            if (vowels.contains(Character.toString(word.charAt(i))) &&
                    !vowels.contains(Character.toString(word.charAt(i - 1))) &&
                    !vowels.contains(Character.toString(word.charAt(i + 1)))) {
                result.append(word.charAt(i));
                break;
            }
        }
        return result.toString();
    }
}

