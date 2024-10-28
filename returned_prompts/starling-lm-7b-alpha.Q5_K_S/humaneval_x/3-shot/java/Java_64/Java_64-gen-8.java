        int count = 0;
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        vowels.add('y');

        for (char c : s.toLowerCase().toCharArray()) {
            if (vowels.contains(c)) {
                count += 1;
            }
        }
        return count;
    }
}

