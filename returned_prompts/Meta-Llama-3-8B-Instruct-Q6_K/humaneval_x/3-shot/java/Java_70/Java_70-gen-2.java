        List<Integer> result = new ArrayList<>();
        List<Integer> sorted = new ArrayList<>(lst);
        Collections.sort(sorted);

        while (!sorted.isEmpty()) {
            result.add(sorted.get(0));
            sorted.remove(0);
            if (!sorted.isEmpty()) {
                int maxIndex = 0;
                for (int i = 1; i < sorted.size(); i++) {
                    if (sorted.get(i) > sorted.get(maxIndex)) {
                        maxIndex = i;
                    }
                }
                result.add(sorted.get(maxIndex));
                sorted.remove(maxIndex);
            }
        }
        return result;
    }
}