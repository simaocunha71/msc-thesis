        Map<Integer, Integer> map = new HashMap<>();
        int max = -1;
        for (int i : lst) {
            map.put(i, map.getOrDefault(i, 0) + 1);
            if (i > max && map.get(i) >= i) {
                max = i;
            }
        }
        return max;
    }
}

*/

