        List<Integer> result = new ArrayList<>(nums);
        result.sort((a, b) -> {
            int sum1 = 0, sum2 = 0;
            while (a > 0) {
                sum1 += a % 10;
                a /= 10;
            }
            while (b > 0) {
                sum2 += b % 10;
                b /= 10;
            }
            if (sum1 == sum2) return nums.indexOf(a) - nums.indexOf(b);
            else return sum1 - sum2;
        });
        return result;
    }
}

