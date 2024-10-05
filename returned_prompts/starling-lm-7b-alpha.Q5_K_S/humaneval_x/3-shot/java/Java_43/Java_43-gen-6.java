        Map<Integer, Integer> element_map = new HashMap<>();
        for (Integer n : l) {
            if (element_map.containsKey(-n)) {
                return true;
            } else {
                Integer n_count = element_map.getOrDefault(n, 0);
                element_map.put(n, n_count + 1);
            }
        }
        return false;
    }
}

