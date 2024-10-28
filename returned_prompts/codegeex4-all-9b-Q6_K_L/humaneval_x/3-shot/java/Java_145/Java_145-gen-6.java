        List<Integer> result = new ArrayList<>(nums);

        for (int i = 0; i < result.size(); i++) {
            for (int j = i + 1; j < result.size(); j++) {
                int i_sum = 0;
                int j_sum = 0;
                for (int n : String.valueOf(result.get(i)).toCharArray()) {
                    i_sum += n - '0';
                }
                for (int n : String.valueOf(result.get(j)).toCharArray()) {
                    j_sum += n - '0';
                }
                if (i_sum > j_sum) {
                    Collections.swap(result, i, j);
                }
            }
        }
        return result;
    }
}

