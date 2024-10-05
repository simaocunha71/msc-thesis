        List<Integer> result = new ArrayList<>();
        if (arr.isEmpty()) return result;

        int minEvenValue = Integer.MAX_VALUE;
        int minEvenIndex = -1;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < minEvenValue) {
                minEvenValue = arr.get(i);
                minEvenIndex = i;
            }
        }

        if (minEvenIndex == -1) return new ArrayList<>();

        result.add(minEvenValue);
        result.add(minEvenIndex);

        return result;
    }
}

