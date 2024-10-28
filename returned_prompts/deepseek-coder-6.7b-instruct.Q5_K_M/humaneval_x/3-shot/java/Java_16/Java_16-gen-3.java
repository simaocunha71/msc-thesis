        Set<Character> distinct_chars = new HashSet<>();
        for  (char c : string.toLowerCase().toCharArray()) {
            distinct_chars.add(c);
        }
        return distinct_chars.size();
     }
}

