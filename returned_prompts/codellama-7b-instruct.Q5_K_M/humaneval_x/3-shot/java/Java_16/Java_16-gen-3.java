        Set<Character> seen = new HashSet<>();
        for (char c : string.toLowerCase().toCharArray()) seen.add(c);
        return seen.size();
    }
}

