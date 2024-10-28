        List<Integer> result = new ArrayList<>();
        List<Integer> remaining = new ArrayList<>(lst);

        while (remaining.size() > 0) {
            Integer min = Collections.min(remaining);
            result.add(min);
            remaining.remove(min);

            if (remaining.size() == 0) break;

            Integer max = Collections.max(remaining);
            result.add(max);
            remaining.remove(max);
        }
        return result;
    }
}

