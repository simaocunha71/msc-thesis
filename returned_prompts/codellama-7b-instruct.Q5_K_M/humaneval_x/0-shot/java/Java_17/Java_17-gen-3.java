        List<Integer> list = new ArrayList<>();
        String[] array = string.split("\\s+");
        for (String s : array) {
            if (s.equals("o")) {
                list.add(4);
            } else if (s.equals("o|")) {
                list.add(2);
            } else {
                list.add(1);
            }
        }
        return list;
    }
}

