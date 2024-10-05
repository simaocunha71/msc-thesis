        List<String> result = new ArrayList<>();
        HashMap<Double, String> map = new HashMap<>();
        map.put(4.0, "A+");
        map.put(3.7, "A");
        map.put(3.3, "A-");
        map.put(3.0, "B+");
        map.put(2.7, "B");
        map.put(2.3, "B-");
        map.put(2.0, "C+");
        map.put(1.7, "C");
        map.put(1.3, "C-");
        map.put(1.0, "D+");
        map.put(0.7, "D");
        map.put(0.0, "D-");
        map.put(0.0, "E");

        for (double grade : grades) {
            result.add(map.get(Math.max(grade, 0.0)));
        }
        return result;
    }
}

