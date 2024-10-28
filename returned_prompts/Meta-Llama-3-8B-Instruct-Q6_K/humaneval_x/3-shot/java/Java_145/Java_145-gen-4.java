        List<Integer> result = new ArrayList<>(nums);
        Collections.sort(result, (a, b) -> {
            int sumA = sumOfDigits(a);
            int sumB = sumOfDigits(b);
            if (sumA != sumB) {
                return Integer.compare(sumA, sumB);
            } else {
                return Integer.compare(result.indexOf(a), result.indexOf(b));
            }
        });
        return result;
    }

    private int sumOfDigits(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}

