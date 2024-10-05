        List<Integer> result = new ArrayList<>();
        List<Integer> sorted_nums = new ArrayList<>(nums);
        Collections.sort(sorted_nums);
        for (int i = 0; i < nums.size(); i++) {
            result.add(nums.get(i));
            result.get(result.size() - 1).sum = sorted_nums.get(i);
        }
        Collections.sort(result, (a, b) -> {
            if (a.sum != b.sum) {
                return Integer.compare(a.sum, b.sum);
            } else {
                return Integer.compare(a.index, b.index);
            }
        });
        return result;
    }
}

