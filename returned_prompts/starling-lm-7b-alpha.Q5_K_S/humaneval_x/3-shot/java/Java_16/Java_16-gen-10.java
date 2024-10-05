        Set<Character> distinct_set = new HashSet<>();

        for (char c : string.toCharArray()) {
            distinct_set.add(c);
        }

        return distinct_set.size();
    }
}

