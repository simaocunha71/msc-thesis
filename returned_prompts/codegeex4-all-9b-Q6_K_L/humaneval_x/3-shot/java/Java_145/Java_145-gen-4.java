        Collections.sort(nums, new Comparator<Integer>() {
            public int compare(Integer x, Integer y) {
                int x_sum = 0;
                int y_sum = 0;
                while (x != 0) {
                    x_sum += x % 10;
                    x /= 10;
                }
                while (y != 0) {
                    y_sum += y % 10;
                    y /= 10;
                }
                return x_sum - y_sum;
            }
        });
        return nums;

    }
}

