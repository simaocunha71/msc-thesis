        List<Integer> result = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) result.add(i);
        }
        return result;
    }

    private boolean isPrime(int num) {
        for (int j = 2; j <= Math.sqrt(num); j++) {
            if (num % j == 0) return false;
        }
        return true;
    }
}

