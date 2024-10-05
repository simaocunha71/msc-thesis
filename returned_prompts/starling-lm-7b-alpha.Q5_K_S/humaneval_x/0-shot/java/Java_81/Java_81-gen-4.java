    List<String> result = new ArrayList<>();

    for (double gpa : grades) {
      if (gpa >= 4.0) {
        result.add("A+");
        continue A;
      }

      if (gpa >= 3.7) {
        result.add("A");
        continue A;
      }

      if (gpa >= 3.3) {
        result.add("A-");
        continue A;
      }

      if (gpa >= 3.0) {
        result.add("B+");
        continue A;
      }

      if (gpa >= 2.7) {
        result.add("B");
        continue A;
      }

      if (gpa >= 2.3) {
        result.add("B-");
        continue A;
      }

      if (gpa >= 2.0) {
        result.add("C+");
        continue A;
      }

      if (gpa >= 1.7) {
        result.add("C");
        continue A;
      }

      if (gpa >= 1.3) {
        result.add("C-");
        continue A;
      }

      if (gpa >= 1.0) {
        result.add("D+");
        continue A;
      }

      if (gpa >= 0.7) {
        result.add("D");
        continue A;
      }

      if (gpa >= 0.0) {
        result.add("D-");
        continue A;
      }
      result.add("E");
    }
    return result;
  }
}





































































































