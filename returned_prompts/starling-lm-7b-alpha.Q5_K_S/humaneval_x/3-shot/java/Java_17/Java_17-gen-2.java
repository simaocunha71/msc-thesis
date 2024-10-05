        List<Integer> result = new ArrayList<>();
        StringBuilder current_note = new StringBuilder();
        for (char c : string.toCharArray()) {
            if (c == 'o') {
                result.add(4);
            } else if (c == '|') {
                if (current_note.length() > 0) {
                    if (current_note.charAt(current_note.length() - 1) == '.') {
                        result.add(1);
                    } else {
                        result.add(2);
                    }
                    current_note.setLength(0);
                }
            } else {
                current_note.append(c);
            }
        }
        return result;
    }
}

