        List<String> gradeList = new ArrayList<String>();
        for (int i = 0; i < grades.size(); i++) {
            if (grades.get(i) >= 4.0) {
                gradeList.add("A+");
            } else if (grades.get(i) >= 3.7) {
                gradeList.add("A");
            } else if (grades.get(i) >= 3.3) {
                gradeList.add("A-");
            } else if (grades.get(i) >= 3.0) {
                gradeList.add("B+");
            } else if (grades.get(i) >= 2.7) {
                gradeList.add("B");
            } else if (grades.get(i) >= 2.3) {
                gradeList.add("B-");
            } else if (grades.get(i) >= 2.0) {
                gradeList.add("C+");
            } else if (grades.get(i) >= 1.7) {
                gradeList.add("C");
            } else if (grades.get(i) >= 1.3) {
                gradeList.add("C-");
            } else if (grades.get(i) >= 1.0) {
                gradeList.add("D+");
            } else if (grades.get(i) >= 0.7) {
                gradeList.add("D");
            } else if (grades.get(i) >= 0.0) {
                gradeList.add("D-");
            } else {
                gradeList.add("E");
            }
        }
        return gradeList;
    }
}
