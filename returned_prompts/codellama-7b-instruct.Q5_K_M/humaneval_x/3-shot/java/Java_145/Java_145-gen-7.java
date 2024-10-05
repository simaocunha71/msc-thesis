        // sort the list
        Collections.sort(nums, new Comparator<Integer>() {
            public int compare(Integer i1, Integer i2) {
                int sum1 = getSum(i1);
                int sum2 = getSum(i2);
                if (sum1 != sum2) return Integer.compare(sum1, sum2);
                else return Integer.compare(i1, i2);
            }
        });
        return nums;
    }

    private int getSum(int i) {
        String s = String.valueOf(i);
        int sum = 0;
        for (int j = 0; j < s.length(); j++) sum += s.charAt(j) - '0';
        return sum;
    }
}

