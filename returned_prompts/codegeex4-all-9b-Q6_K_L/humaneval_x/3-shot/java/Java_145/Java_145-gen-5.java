        Collections.sort(nums, new Comparator<Integer>() {
            @Override
            public int compare(Integer x, Integer y) {
                int sum_x = 0;
                int sum_y = 0;

                for (char c : x.toString().toCharArray()) {
                    sum_x += Character.getNumericValue(c);
                }

                for (char c : y.toString().toCharArray()) {
                    sum_y += Character.getNumericValue(c);
                }

                if (sum_x == sum_y) return x - y;
                else return sum_x - sum_y;
            }
        });
        return nums;
    }
}

