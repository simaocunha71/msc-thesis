
        // Corner case
        if (word == null || word.length() < 3) {
            return "";
        }

        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        int closest = Integer.MAX_VALUE;
        char closestLetter = ' ';
        for (int i = 1; i < word.length() - 1; i++) {
            if (!vowels.contains(word.charAt(i))) {
                continue;
            }
            int diff = Math.abs(i - (word.charAt(i - 1) == ' ' ? 0 : i - 1))
                    + Math.abs(i - (word.charAt(i + 1) == ' ' ? word.length() : i + 1));
            if (diff < closest) {
                closest = diff;
                closestLetter = word.charAt(i);
            }
        }

        return "" + closestLetter;
    }
}

































































































































































































































