        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            boolean hasEvenDigit = false;
            int numCopy = num;
            while (numCopy > 0) {
                int digit = numCopy % 10;
                if (digit % 2 == 0) {
                    hasEvenDigit = true;
                    break;
                }
                numCopy /= 10;
            }
            if (!hasEvenDigit) result.add(num);
        }
        Collections.sort(result);
        return result;
    }
}

