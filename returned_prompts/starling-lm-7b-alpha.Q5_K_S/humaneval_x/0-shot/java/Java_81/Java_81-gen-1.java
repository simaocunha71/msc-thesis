        List<String> result = new ArrayList<>();
        for (double gpa : grades) {
            switch (true) {
                case (gpa > 4.0):
                    result.add("A+");
                    break A;
                case (gpa > 3.7):
                    result.add("A");
                    break A;
                case (gpa > 3.3):
                    result.add("A-");
                    break A;
                case (gpa > 3.0):
                    result.add("B+");
                    break A;
                case (gpa > 2.7):
                    result.add("B");
                    break A;
                case (gpa > 2.3):
                    result.add("B-");
                    break A;
                case (gpa > 2.0):
                    result.add("C+");
                    break A;
                case (gpa > 1.7):
                    result.add("C");
                    break A;
                case (gpa > 1.3):
                    result.add("C-");
                    break A;
                case (gpa > 1.0):
                    result.add("D+");
                    break A;
                case (gpa > 0.7):
                    result.add("D");
                    break A;
                case (gpa > 0.0):
                    result.add("D-");
                    break A;
                case (gpa == 0.0):
                    result.add("E");
                    break A;
                default:
                    break;
            }
        }
        return result;
    }
}





















































































