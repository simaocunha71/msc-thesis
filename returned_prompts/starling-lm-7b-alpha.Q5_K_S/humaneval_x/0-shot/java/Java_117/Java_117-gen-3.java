        List<String> result = new ArrayList<>();
        Set<Character> consonants = new HashSet<>(Arrays.asList('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'));
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) {
                int count = 0;
                int j = i;
                while (j < s.length() && (s.charAt(j) == ' ' || consonants.contains(s.charAt(j)))) {
                    if (s.charAt(j) == ' ' && count == n) {
                        result.add(s.substring(i, j + 1));
                        i = j;
                        continue A;
                    }
                    if (Character.isLetter(s.charAt(j)) && consonants.contains(s.charAt(j))) {
                        count++;
                    }
                    j++;
                }
                if (count == n && j == s.length()) {
                    result.add(s.substring(i, j + 1));
                }
            }
        }
        return result;
    }
}







































































































































































