        List<Integer> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;

        for (int num : numbers) {
            if (num > max) {
                max = num;
            }
            result.add(max);
        }
        return result;
     }
}

