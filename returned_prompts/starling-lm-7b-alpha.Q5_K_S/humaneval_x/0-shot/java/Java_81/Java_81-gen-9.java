    List<String> result = new ArrayList<>();
    Collections.sort(grades);
    for (double g : grades) {
        if (g >= 4.0) {
            result.add("A+");
            continue A;
        }
        if (g >= 3.7) {
            result.add("A");
            continue A;
        }
        if (g >= 3.3) {
            result.add("A-");
            continue A;
        }
        if (g >= 3.0) {
            result.add("B+");
            continue A;
        }
        if (g >= 2.7) {
            result.add("B");
            continue A;
        }
        if (g >= 2.3) {
            result.add("B-");
            continue A;
        }
        if (g >= 2.0) {
            result.add("C+");
            continue A;
        }
        if (g >= 1.7) {
            result.add("C");
            continue A;
        }
        if (g >= 1.3) {
            result.add("C-");
            continue A;
        }
        if (g >= 1.0) {
            result.add("D+");
            continue A;
        }
        if (g >= 0.7) {
            result.add("D");
            continue A;
        }
        if (g >= 0.0) {
            result.add("D-");
            continue A;
        }
        result.add("E");
    }
    return result;
    }
}






















































































































