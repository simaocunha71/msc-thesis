    public List<Integer> rollingMax(List<Integer> numbers) {
        List<Integer> maxList = new ArrayList<>();
        int maxSoFar = Integer.MIN_VALUE;
        for (int num : numbers) {
            maxList.add(Math.max(num, maxSoFar));
            maxSoFar = Math.max(maxSoFar, num);
        }
        return maxList;
    }
}