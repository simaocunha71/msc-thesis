        List<Integer> result = new ArrayList<>();

        Map<Integer, Integer> l1_map = new HashMap<>();
        for (int i : l1) {
            l1_map.put(i, l1_map.getOrDefault(i, 0) + 1);
        }

        for (int i : l2) {
            if (l1_map.containsKey(i)) {
                result.add(i);
                if (l1_map.get(i) == 1) l1_map.remove(i);
                else l1_map.put(i, l1_map.get(i) - 1);
            }
        }

        return result;
    }
}

