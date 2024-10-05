        List<Integer> result = new ArrayList<>();
        TreeSet<Integer> remaining = new TreeSet<>(lst);
        while (!remaining.isEmpty()) {
            result.add(remaining.first());
            remaining.remove(remaining.first());
            result.add(remaining.last());
            remaining.remove(remaining.last());
        }
        return result;
    }
}

