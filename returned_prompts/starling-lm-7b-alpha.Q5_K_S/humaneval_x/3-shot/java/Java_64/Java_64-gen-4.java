        int count = 0;
        HashSet<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'y'));
        for (char c : s.toLowerCase().toCharArray()) {
            if (vowels.contains(c)) count += 1;
        }
        return count;
    }
}

