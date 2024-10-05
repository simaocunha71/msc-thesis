        List<Integer> result = new ArrayList<>();
        List<Integer> sorted = new ArrayList<>(lst);
        Collections.sort(sorted);

        while (!sorted.isEmpty()) {
            result.add(sorted.remove(0));
            if (!sorted.isEmpty()) result.add(sorted.remove(sorted.size() - 1));
        }

        return result;
    }
}

