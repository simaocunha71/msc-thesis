        List<String> result = new ArrayList<>();
        for (double grade : grades) {
            if (grade >= 4.0) {
                result.add("A+");
            } else if (grade > 3.7) {
                result.add("A");
            } else if (grade > 3.3) {
                result.add("A-");
            } else if (grade > 3.0) {
                result.add("B+");
            } else if (grade > 2.7) {
                result.add("B");
            } else if (grade > 2.3) {
                result.add("B-");
            } else if (grade > 2.0) {
                result.add("C+");
            } else if (grade > 1.7) {
                result.add("C");
            } else if (grade > 1.3) {
                result.add("C-");
            } else if (grade > 1.0) {
                result.add("D+");
            } else if (grade > 0.7) {
                result.add("D");
            } else if (grade > 0.0) {
                result.add("D-");
            } else {
                result.add("E");
            }
        }
        return result;
    }
}

