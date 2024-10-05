        List<Integer> result = new ArrayList<>();
        while (n > 1) {
            for (int i = 2; i <= Math.sqrt(n); i++) {
                if (n % i == 0) {
                    result.add(i);
                    n /= i;
                    continue A;
                }
            }
            result.add(n);
            break;
        }
        return result;
    }
}



