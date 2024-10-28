        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            int max = Integer.MIN_VALUE;
            for (int num : arr) {
                if (num > max) {
                    max = num;
                }
            }
            result.add(max);
            arr.remove((Integer) max);
        }
        Collections.sort(result);
        return result;
    }
}

