        List<Integer> result = new ArrayList<>();
        int currentMax = Integer.MIN_VALUE;

        for (int num : numbers) {
            currentMax = Math.max(currentMax, num);
            result.add(currentMax);
        }

        return result;
    }
}

