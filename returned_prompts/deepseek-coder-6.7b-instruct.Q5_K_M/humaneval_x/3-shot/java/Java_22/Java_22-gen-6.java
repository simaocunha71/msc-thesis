        List<Integer> integers = new ArrayList<>();
        for  (Object value : values) {
            if  (value instanceof Integer) {
                integers.add((Integer) value);
            }
        }
        return integers;
     }
}

