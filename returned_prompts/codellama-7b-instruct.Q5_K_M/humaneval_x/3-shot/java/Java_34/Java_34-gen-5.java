        List<Integer> result = new ArrayList<>(l.size());
        Set<Integer> seen = new HashSet<>(l.size());
        for (int i = 0; i < l.size(); i++) {
            int n = l.get(i);
            if (!seen.contains(n)) {
                result.add(n);
                seen.add(n);
            }
        }
        Collections.sort(result);
        return result;
    }
}

