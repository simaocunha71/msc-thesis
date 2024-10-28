        String[] split_string = string.split(" ");

        List<Integer> result = new ArrayList<>();

        for (String s : split_string) {
            if (s.equals("o")) {
                result.add(4);
            } else if (s.equals("o|")) {
                result.add(2);
            } else if (s.equals(".|")) {
                result.add(1);
            }
        }
        return result;
    }
}

