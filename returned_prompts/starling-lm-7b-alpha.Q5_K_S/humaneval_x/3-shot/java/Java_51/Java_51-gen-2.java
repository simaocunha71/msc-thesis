        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        vowels.add('y');
        vowels.add('A');
        vowels.add('E');
        vowels.add('I');
        vowels.add('O');
        vowels.add('U');
        vowels.add('Y');
        StringBuilder result = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (!vowels.contains(c)) {
                result.append(c);
            }
        }
        return result.toString();
    }
}



```