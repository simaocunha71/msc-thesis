        Map<Integer, Integer> counts = new HashMap<>();

        for  (int num : lst) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }

        for  (int i = lst.size(); i > 0; i--) {
            if  (counts.containsKey(i) && counts.get(i) >= i) {
                return i;
            }
        }
        return -1;
    }
}

