        List<Integer> result = Arrays.asList(0, 0);
        num = Math.abs(num);
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                result.set(0, result.get(0) + 1);
            } else {
                result.set(1, result.get(1) + 1);
            }
            num = num / 10;
        }
        return result;
     }
}

