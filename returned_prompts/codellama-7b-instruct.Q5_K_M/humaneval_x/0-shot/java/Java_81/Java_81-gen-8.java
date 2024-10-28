        for (int i = 0; i < grades.size(); i++) {
            if (grades.get(i) == 4.0) {
                grades.set(i, "A+");
                continue A;
            }
            if (grades.get(i) > 3.7) {
                grades.set(i, "A");
                continue A;
            }
            if (grades.get(i) > 3.3) {
                grades.set(i, "A-");
                continue A;
            }
            if (grades.get(i) > 3.0) {
                grades.set(i, "B+");
                continue A;
            }
            if (grades.get(i) > 2.7) {
                grades.set(i, "B");
                continue A;
            }
            if (grades.get(i) > 2.3) {
                grades.set(i, "B-");
                continue A;
            }
            if (grades.get(i) > 2.0) {
                grades.set(i, "C+");
                continue A;
            }
            if (grades.get(i) > 1.7) {
                grades.set(i, "C");
                continue A;
            }
            if (grades.get(i) > 1.3) {
                grades.set(i, "C-");
                continue A;
            }
            if (grades.get(i) > 1.0) {
                grades.set(i, "D+");
                continue A;
            }
            if (grades.get(i) > 0.7) {
                grades.set(i, "D");
                continue A;
            }
            if (grades.get(i) > 0.0) {
                grades.set(i, "D-");
                continue A;
            }
            if (grades.get(i) == 0.0) {
                grades.set(i, "E