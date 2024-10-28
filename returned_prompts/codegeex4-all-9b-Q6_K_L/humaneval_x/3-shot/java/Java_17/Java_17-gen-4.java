        List<Integer> result = new ArrayList<>();
        Map<Character, Integer> notes = new HashMap<>();
        notes.put('o', 4);
        notes.put('o', 2);
        notes.put('.', 1);

        for (char c : string.toCharArray()) {
            if (notes.containsKey(c)) {
                result.add(notes.get(c));
            }
        }
        return result;
    }
}

