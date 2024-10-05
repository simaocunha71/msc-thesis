        List<Integer> result = new ArrayList<>();
        List<Integer> remaining_values = new ArrayList<>(lst);
        while (remaining_values.size() != 0) {
            result.add(Collections.min(remaining_values));
            remaining_values.remove(Collections.min(remaining_values));
            result.add(Collections.max(remaining_values));
            remaining_values.remove(Collections.max(remaining_values));
        }
        return result;
    }
}

