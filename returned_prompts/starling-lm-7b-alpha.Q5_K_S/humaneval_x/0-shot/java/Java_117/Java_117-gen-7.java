        List<String> result = new ArrayList<>();

        Set<Character> consonants = new HashSet<>();
        consonants.add('b'); consonants.add('c'); consonants.add('d'); consonants.add('f'); consonants.add('g');
        consonants.add('h'); consonants.add('j'); consonants.add('k'); consonants.add('l'); consonants.add('m');
        consonants.add('n'); consonants.add('p'); consonants.add('q'); consonants.add('r'); consonants.add('s');
        consonants.add('t'); consonants.add('v'); consonants.add('w'); consonants.add('x'); consonants.add('y');
        consonants.add('z');

        for (int i = 0; i < s.length(); i++) {
            if (i == 0 || s.charAt(i) == ' ') {
                int count = 0;
                int j = i;
                while (j < s.length()) {
                    char c = s.charAt(j);
                    if (consonants.contains(c)) {
                        count++;
                    }
                    if (count == n) {
                        result.add(s.substring(i, j + 1));
                        break;
                    } else if (!consonants.contains(c)) {
                        if (c == ' ') {
                            result.add(s.substring(i, j + 1));
                            break;
                        }
                        i = j;
                    }
                    j++;
                }
            }
        }
        return result;
    }
}

















































































