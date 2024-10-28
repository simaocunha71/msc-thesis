        List<String> result = new ArrayList<>();
        Map<Double, Character> letter_grade_map = new HashMap<>();
        letter_grade_map.put(4.0, 'A');
        letter_grade_map.put(3.7, 'A');
        letter_grade_map.put(3.3, 'A');
        letter_grade_map.put(3.0, 'B');
        letter_grade_map.put(2.7, 'B');
        letter_grade_map.put(2.3, 'B');
        letter_grade_map.put(2.0, 'C');
        letter_grade_map.put(1.7, 'C');
        letter_grade_map.put(1.3, 'C');
        letter_grade_map.put(1.0, 'D');
        letter_grade_map.put(0.7, 'D');
        letter_grade_map.put(0.0, 'E');

        for (double grade : grades) {
            Character letter_grade = letter_grade_map.higherKey(grade);
            result.add(letter_grade.toString());
        }
        return result;
    }
}

