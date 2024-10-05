        List<Integer> result = new ArrayList<>();
        List<Integer> remain = new ArrayList<>(lst);
        while (!remain.isEmpty()) {
            result.add(Collections.min(remain));
            remain.removeIf(v -> v == result.get(result.size() - 1));
            result.add(Collections.max(remain));
            remain.removeIf(v -> v == result.get(result.size() - 1));
        }
        return result;
    }
}

