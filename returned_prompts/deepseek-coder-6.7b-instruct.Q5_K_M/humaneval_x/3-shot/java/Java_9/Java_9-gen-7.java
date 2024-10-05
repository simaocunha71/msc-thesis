        List<Integer> result = new ArrayList<>();
        int currentMax = Integer.MIN_VALUE;
        for (int number : numbers) {
            currentMax = Math.max(currentMax, number);
            result.add(currentMax);
        }
        return result;
     }
}

