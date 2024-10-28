        List<Integer> result = new ArrayList<>();
        int min = Integer.MAX_VALUE;
        int index = -1;

        for (int i = 0; i < arr.size(); i++) {
            int value = arr.get(i);
            if (value % 2 == 0 && value < min) {
                min = value;
                index = i;
            }
        }

        if (min == Integer.MAX_VALUE) return result;
        else {
            result.add(min);
            result.add(index);
            return result;
        }
    }
}

