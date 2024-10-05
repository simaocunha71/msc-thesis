        List<Integer> result = new ArrayList<>();
        StringBuilder note = new StringBuilder();
        for (char c : string.toCharArray()) {
            if (c == 'o') {
                note.append("o");
                result.add(4);
            } else if (c == '|') {
                if (note.length() > 0) {
                    if (note.charAt(note.length() - 1) == 'o') {
                        result.add(2);
                    } else {
                        result.add(1);
                    }
                    note.setLength(0);
                }
            } else if (c == '.') {
                note.append(".");
            }
        }
        return result;
    }
}

