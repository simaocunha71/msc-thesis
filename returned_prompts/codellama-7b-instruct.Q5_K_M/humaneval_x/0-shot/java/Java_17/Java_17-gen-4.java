        List<Integer> output = new ArrayList<Integer>();
        String[] input = string.split(" ");

        for (String i : input) {
            if (i.equals("o")) {
                output.add(4);
            } else if (i.equals("o|")) {
                output.add(2);
            } else if (i.equals(".|")) {
                output.add(1);
            } else {
                output.add(0);
            }
        }

        return output;
    }
}