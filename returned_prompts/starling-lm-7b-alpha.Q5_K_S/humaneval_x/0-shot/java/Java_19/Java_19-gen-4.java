    // Convert String array to int array
    int[] arr = new int[numbers.length()];
    int index = 0;
    for (String s : numbers.split(" ")) {
      arr[index++] = Integer.parseInt(s);
    }

    Arrays.sort(arr);

    StringBuilder sb = new StringBuilder();
    for (int i : arr) {
      if (i == 0) {
        sb.append("zero ");
      } else if (i == 1) {
        sb.append("one ");
      } else if (i == 2) {
        sb.append("two ");
      } else if (i == 3) {
        sb.append("three ");
      } else if (i == 4) {
        sb.append("four ");
      } else if (i == 5) {
        sb.append("five ");
      } else if (i == 6) {
        sb.append("six ");
      } else if (i == 7) {
        sb.append("seven ");
      } else if (i == 8) {
        sb.append("eight ");
      } else if (i == 9) {
        sb.append("nine ");
      }
    }
    return sb.toString().trim();
  }
}










































































































































































































