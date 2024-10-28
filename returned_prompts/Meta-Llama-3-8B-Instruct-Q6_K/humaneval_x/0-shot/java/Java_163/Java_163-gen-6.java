    if (a > b) {
        int temp = a;
        a = b;
        b = temp;
    }
    List<Integer> result = new ArrayList<>();
    for (int i = a; i <= b; i++) {
        String str = String.valueOf(i);
        for (int j = 0; j < str.length(); j++) {
            if (str.charAt(j) % 2 == 0) {
                result.add(Integer.parseInt(str.substring(j, j + 1)));
            }
        }
    }
    return result;
}  // return the even digits between a and b, in ascending order.
}

