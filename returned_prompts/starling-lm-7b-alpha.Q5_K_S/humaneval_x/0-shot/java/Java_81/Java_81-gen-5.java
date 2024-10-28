    List<String> letterGradeList = new ArrayList<>();
    for (double grade : grades) {
      if (grade >= 4.0) {
        letterGradeList.add("A+");
      } else if (grade >= 3.7) {
        letterGradeList.add("A");
      } else if (grade >= 3.3) {
        letterGradeList.add("A-");
      } else if (grade >= 3.0) {
        letterGradeList.add("B+");
      } else if (grade >= 2.7) {
        letterGradeList.add("B");
      } else if (grade >= 2.3) {
        letterGradeList.add("B-");
      } else if (grade >= 2.0) {
        letterGradeList.add("C+");
      } else if (grade >= 1.7) {
        letterGradeList.add("C");
      } else if (grade >= 1.3) {
        letterGradeList.add("C-");
      } else if (grade >= 1.0) {
        letterGradeList.add("D+");
      } else if (grade >= 0.7) {
        letterGradeList.add("D");
      } else if (grade >= 0.0) {
        letterGradeList.add("D-");
      } else {
        letterGradeList.add("E");
      }
    }

    return letterGradeList;
  }
}


















































































































































