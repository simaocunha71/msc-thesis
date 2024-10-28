        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < l.size(); i++) {
            int target = -l.get(i);
            if (seen.get(target) != null) {
                return true;
            }
            seen.put(l.get(i), seen.getOrDefault(l.get(i), 0) + 1);
        }
        return false;
    }
}

