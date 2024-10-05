        List<Integer> result = new ArrayList<>();
        int current_beats = 0;
        String[] notes = string.split(" ");

        for (String note : notes) {
            if (note.equals("o")) {
                current_beats += 4;
            } else if (note.equals("o|")) {
                current_beats += 2;
            } else if (note.equals(".|")) {
                current_beats += 1;
            }
            result.add(current_beats);
        }
        return result;
    }
}