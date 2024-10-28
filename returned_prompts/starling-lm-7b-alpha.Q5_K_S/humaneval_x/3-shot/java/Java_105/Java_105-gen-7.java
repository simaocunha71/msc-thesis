        Collections.sort(arr);
        Collections.reverse(arr);
        List<String> result = new ArrayList<>();

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < 0 || arr.get(i) > 9) {
                result.add(getNumberName(-1));
                continue;
            }
            result.add(getNumberName(arr