        Collections.sort(nums, new Comparator<Integer>() {
            public int compare(Integer a, Integer Integer) {
                int sumA = sumOfDigits(a);
                int sumB = sumOfDigits(b);
                if (sumA != sumB) return sumA - sumB;
                return Integer.compare(a, b);
            }

            private int sumOfDigits(int number) {
                int sum = 0;
                while (number > 0) {
                    sum += number % 10;
                    number /= 10;
                }
                return sum;
            }
        });
        return nums;
    }
}

