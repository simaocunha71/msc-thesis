        Set<Integer> unique_set = new TreeSet<>();
        for (int i : l) {
            unique_set.add(i);
        }
        List<Integer> result = new ArrayList<>();
        for (int i : unique_set) {
            result.add(i);
        }
        Collections.sort(result);
        return result;
    }
}

