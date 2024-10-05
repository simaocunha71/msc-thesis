        List<Integer> result = new ArrayList<Integer>();

        int evenCount = 0;
        int oddCount = 0;

        while (num != 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
            num /= 10;
        }

        result.add(evenCount);
        result.add(oddCount);

        return result;
    }
}
