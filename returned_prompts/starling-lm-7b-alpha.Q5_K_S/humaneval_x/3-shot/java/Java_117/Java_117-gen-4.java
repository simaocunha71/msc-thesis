        List<String> result = new ArrayList<>();
        HashSet<Character> consonants = new HashSet<>();
        consonants.add('b');
        consonants.add('c');
        consonants.add('d');
        consonants.add('f');
        consonants.add('g');
        consonants.add('h');
        consonants.add('j');
        consonants.add('k');
        consonants.add('l');
        consonants.add('m');
        consonants.add('n');
        consonants.add('p');
        consonants.add('q');
        consonants.add('r');
        consonants.add('s');
        consonants.add('t');
        consonants.add('v');
        consonants.add('w');
        consonants.add('x');
        consonants.add('y');
        consonants.add('z');

        for (String word : s.split(" ")) {
            int n_consonants = 0;
            for (char c : word.toCharArray()) {
                if (consonants.contains(c)) {
                    n_consonants += 1;
                }
            }
            if (n_consonants == n) {
                result.add(word);
            }
        }
        return result;
    }
}

