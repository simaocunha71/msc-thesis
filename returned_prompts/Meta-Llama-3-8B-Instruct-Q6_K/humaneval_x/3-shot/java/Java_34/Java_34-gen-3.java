        Set<Integer> set = new LinkedHashSet<>();
        for (Integer i : l) {
            set.add(i);
        }
        List<Integer> result = new ArrayList<>(set);
        Collections.sort(result);
        return result;
    }
}

