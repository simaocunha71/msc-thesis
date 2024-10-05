        List<String> res = new ArrayList<>();

        Map<Double, String> map = new HashMap<>();
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
            if (map.containsKey(grade)) {
                res.add(map.get(grade));
            } else {
                if (grade < 0.0) {
                    throw new IllegalArgumentException("Invalid GPA: " + grade);
                }
                if (grade < 1.0) {
                    res.add("D+");
                } else if (grade < 1.3) {
                    res.add("D");
                } else if (grade < 1.7) {
                    res.add("D-");
                } else if (grade < 2.0) {
                    res.add("C+");
                } else if (grade < 2.3) {
                    res.add("C");
                } else if (grade < 2.7) {
                    res.add("C-");
                } else if (grade < 3.0) {
                    res.add("B+");
                } else if (grade < 3.3) {
                    res.add("B");
                } else if (grade < 3.7) {
                    res.add("B-");
                } else if (grade < 4.0) {
                