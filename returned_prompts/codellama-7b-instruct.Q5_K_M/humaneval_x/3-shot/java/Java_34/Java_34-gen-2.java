        List<Integer> result = new ArrayList<>();
        Set<Integer> seen = new HashSet<>();
        for (int i : l) {
            if (!seen.contains(i)) {
                result.add(i);
                seen.add(i);
            }
        }
        Collections.sort(result);
        return result;
    }
}

