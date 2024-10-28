    public List<Integer> derivative(List<Integer> xs) {
        List<Integer> result = new ArrayList<>();
        result.add(xs.get(1));
        for (int i = 2; i < xs.size(); i++) {
            result.add(i * xs.get(i));
        }
        return result;
    }