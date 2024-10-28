        List<Integer> res = new ArrayList<>();

        // 1. find the minimum even value
        int minEvenValue = Integer.MAX_VALUE;
        int minEvenIndex = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < minEvenValue) {
                minEvenValue = arr.get(i);
                minEvenIndex = i;
            }
        }

        // 2. return the node if we found one
        if (minEvenIndex != -1) {
            res.add(minEvenValue);
            res.add(minEvenIndex);
            return res;
        }

        return res;

    }
}




























