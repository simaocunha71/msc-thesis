        List<Integer> result = new ArrayList<>();
        List<Integer> remaining = new ArrayList<>(lst);

        while (!remaining.isEmpty()) {
            int min = Collections.min(remaining);
            result.add(min);
            remaining.remove(min);

            int max = Collections.max(remaining);
            result.add(max);
            remaining.remove(max);
        }
        return result;
    }
}

