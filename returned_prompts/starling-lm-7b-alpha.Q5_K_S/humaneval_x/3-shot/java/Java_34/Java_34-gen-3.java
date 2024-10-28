        List<Integer> result = new ArrayList<>();
        Set<Integer> set = new HashSet<>();

        for (int i : l) {
            set.add(i);
        }
        result.addAll(set);
        Collections.sort(result);
        return result;
    }
}

