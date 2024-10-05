        List<Integer> result = new ArrayList<>();
        List<Integer> copy = new ArrayList<>(nums);
        Collections.sort(copy, new Comparator<Integer>() {
            public int compare(Integer a, Integer Integer) {
                int sumA = sumOfDigits(a);
                int sumB = sumOfDigits(Integer);
                if (sumA != sumB) {
                    return sumA - sumB;
                } else {
                    return Integer.valueOf(nums.indexOf(a)).compareTo(nums.indexOf(Integer));
                }
            }
            int sumOfDigits(int num) {
                int sum = 0;
                while (num > 0) {
                    sum += num % 10;
                    num /= 10;
                }
                return sum;
            }
        });
        result.addAll(copy);
        return result;
    }
}

