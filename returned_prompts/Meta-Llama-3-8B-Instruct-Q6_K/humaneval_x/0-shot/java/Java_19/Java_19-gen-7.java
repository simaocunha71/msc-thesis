    String[] numArray = numbers.split("\\s+");
    Arrays.sort(numArray);
    StringBuilder sb = new StringBuilder();
    for (String num : numArray) {
        sb.append(num).append(" ");
    }
    return sb.toString().trim();
}
