        List<Integer> result = new ArrayList<>();
        List<Integer> copy = new ArrayList<>(lst);

        while (!copy.isEmpty()) {
            int min = Collections.min(copy);
            result.add(min);
            copy.remove((Integer) min);

            if (!copy.isEmpty()) {
                int max = Collections.max(copy);
                result.add(max);
                copy.remove((Integer) max);
            }
        }
        return result;
    }
}

