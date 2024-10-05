        List<Integer> counts = Arrays.asList(0, 0); // [even, odd]
        for (char c : Integer.toString(Math.abs(num)).toCharArray()) {
            int digit = c - '0';
            counts.set(digit % 2, counts.get(digit % 2) + 1);
        }
        return counts;
     }
}

