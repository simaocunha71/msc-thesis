        List<Integer> result = new ArrayList<>();
        for (String note : string.split(" ")) {
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