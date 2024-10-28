        List<Integer> result = new ArrayList<>();
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < numbers.size(); i++) {
            result.add(max = Math.max(max, numbers.get(i)));
        }
        return result;
    }
}

