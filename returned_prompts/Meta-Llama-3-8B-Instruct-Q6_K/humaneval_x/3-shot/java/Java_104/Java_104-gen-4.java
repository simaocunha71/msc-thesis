        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            int decimal = num;
            boolean hasEvenDigit = false;
            while (decimal > 0) {
                int digit = decimal % 10;
                if (digit % 2 == 0) {
                    hasEvenDigit = true;
                    break;
                }
                decimal /= 10;
            }
            if (!hasEvenDigit) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }
}

