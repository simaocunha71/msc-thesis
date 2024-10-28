        List<Integer> result = new ArrayList<>();
        for (int i : arr) {
            int ones = Integer.bitCount(i);
            int index = 0;
            for (int j = 0; j < result.size(); j++) {
                int temp = result.get(j);
                if (Integer.bitCount(temp) < ones) {
                    index = j + 1;
                    break;
                }
            }
            result.add(index, i);
        }
        return result;
    }
}
