        List<Integer> result = new ArrayList<>();
        for (int i : x) {
            boolean hasEvenDigit = false;
            int n = i;
            while (n > 0) {
                int digit = n % 10;
                if (digit % 2 == 0) {
                    hasEvenDigit = true;
                    break;
                }
                n /= 10;
            }
            if (!hasEvenDigit) result.add(i);
        }
        Collections.sort(result);
        return result;
    }
}

