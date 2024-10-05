        List<Integer> counts = Arrays.asList(0, 0); // [even, odd]
        num = Math.abs(num); // handle negative numbers
        while(num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                counts.set(0, counts.get(0) + 1);
            } else {
                counts.set(1, counts.get(1) + 1);
            }
            num /= 10;
        }
        return counts;
     }
}

