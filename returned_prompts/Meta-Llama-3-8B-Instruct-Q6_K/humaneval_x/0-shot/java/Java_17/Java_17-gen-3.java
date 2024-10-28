    public List<Integer> parseMusic(String string) {
        List<Integer> result = new ArrayList<>();
        String[] notes = string.split(" ");
        for (String note : notes) {
            if (note.equals("o")) {
                result.add(4);
            } else if (note.equals("o|")) {
                result.add(2);
            } else if (note.equals(".|")) {
                result.add(1);
            }
        }
        return result;
    }
}