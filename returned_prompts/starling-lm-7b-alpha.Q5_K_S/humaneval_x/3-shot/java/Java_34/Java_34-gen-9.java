        List<Integer> result = new ArrayList<>();
        Set<Integer> temp_set = new HashSet<>();
        for (Integer i : l) {
            temp_set.add(i);
        }
        result.addAll(temp_set);
        Collections.sort(result);
        return result;
    }
}

