        List<String> result = new ArrayList<>();
        Map<Double, Character> boundaries = new HashMap<>();
        boundaries.put(4.0, 'A');
        boundaries.put(3.7, 'A');
        boundaries.put(3.3, 'A');
        boundaries.put(3.0, 'B');
        boundaries.put(2.7, 'B');
        boundaries.put(2.3, 'B');
        boundaries.put(2.0, 'C');
        boundaries.put(1.7, 'C');
        boundaries.put(1.3, 'C');
        boundaries.put(1.0, 'D');
        boundaries.put(0.7, 'D');
        boundaries.put(0.0, 'D');
        boundaries.put(0.0, 'E');

        for (double gpa : grades) {
            double key = boundaries.lowerKey(gpa);
            result.add(String.valueOf(boundaries.get(key)));
        }
        return result;
    }
}

