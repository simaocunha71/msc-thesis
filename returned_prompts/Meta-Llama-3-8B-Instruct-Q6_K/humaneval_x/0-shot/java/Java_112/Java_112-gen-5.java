    List<Object> result = new ArrayList<>();
    StringBuilder sb = new StringBuilder();
    for (char ch : s.toCharArray()) {
        boolean isPresent = false;
        for (char cch : c.toCharArray()) {
            if (ch == cch) {
                isPresent = true;
                break;
            }
        }
        if (!isPresent) {
            sb.append(ch);
        }
    }
    String str = sb.toString();
    result.add(str);
    result.add(str.equals(new StringBuilder(str).reverse().toString()));
    return result;
}

