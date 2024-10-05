        List<Integer> result = new ArrayList<>();
        int current_note_length = 0;

        for (char c : string.toCharArray()) {
            if (c == 'o') {
                result.add(4);
                current_note_length = 4;
            } else if (c == '|') {
                if (current_note_length == 4) {
                    result.add(2);
                    current_note_length = 2;
                } else if (current_note_length == 2) {
                    result.add(1);
                    current_note_length = 1;
                }
            }
        }
        return result;
    }
}

