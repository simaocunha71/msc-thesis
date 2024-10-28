        List<Integer> result = new ArrayList<>();
        List<Integer> filtered = new ArrayList<>();

        for (int i : x) {
            int temp = i;
            while (temp > 0) {
                if (temp % 10 % 2 == 0) {
                    temp /= 10;
                } else {
                    temp = 0;
                }
            }
            if (temp == 0) {
                result.add(i);
            }
        }

        for (int i : result) {
            if (result.indexOf(i) == result.lastIndexOf(i)) {
                filtered.add(i);
            }
        }
        return filtered;
    }
}
