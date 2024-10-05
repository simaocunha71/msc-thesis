        List<Integer> result = new ArrayList<>();
        a = Math.min(a, b);
        b = Math.max(a, b);
        for (int i = a; i <= b; i++) {
            String str = Integer.toString(i);
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) % 2 == 0) {
                    result.add(Integer.parseInt(str.substring(j, j + 1)));
                }
            }
        }
        return result;
    }
}
