        List<Integer> result = new ArrayList<>();
        int max_so_far = Integer.MIN_VALUE;

        for (int num : numbers) {
            max_so_far = Math.max(max_so_far, num);
            result.add(max_so_far);
        }
        return result;
    }
}

