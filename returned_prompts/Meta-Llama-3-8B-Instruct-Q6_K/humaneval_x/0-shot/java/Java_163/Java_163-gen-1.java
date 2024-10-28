    List<Integer> result = new ArrayList<>();
    for (int i = Math.min(a, b); i <= Math.max(a, b); i++) {
        String str = String.valueOf(i);
        for (int j = 0; j < str.length(); j++) {
            if (Character.getNumericValue(str.charAt(j)) % 2 == 0) {
                result.add(i);
                break;
            }
        }
    }
    return result;
}

