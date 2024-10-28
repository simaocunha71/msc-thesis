        List<Integer> result = new ArrayList<>();
        Map<Integer, Integer> occurrence_count = new HashMap<>();

        for (int e : l) {
            occurrence_count.merge(e, 1, Integer::sum);
        }

        for (Map.Entry<Integer, Integer> e : occurrence_count.entrySet()) {
            if (e.getValue() == 1) {
                result.add(e.getKey());
            }
        }
        Collections.sort(result);

        return result;
    }
}

