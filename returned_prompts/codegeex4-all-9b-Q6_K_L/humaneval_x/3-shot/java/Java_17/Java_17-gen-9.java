        List<Integer> result = new ArrayList<>();
        String[] notes = string.split("\\s+");
        for (String note : notes) {
            switch (note) {
                case "o":
                    result.add(4);
                    break;
                case "o|":
                    result.add(2);
                    break;
                case ".|":
                    result.add(1);
                    break;
                default:
                    throw new IllegalArgumentException("Invalid note: " + note);
            }
        }
        return result;
    }
}

