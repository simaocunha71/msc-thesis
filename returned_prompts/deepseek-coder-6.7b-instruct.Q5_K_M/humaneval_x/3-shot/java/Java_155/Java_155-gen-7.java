        List<Integer> counts = new ArrayList<>(Arrays.asList(0, 0)); // [even, odd]
        for(char digit : Integer.toString(Math.abs(num)).toCharArray()) {
            counts.set(Character.getNumericValue(digit) % 2, counts.get(Character.getNumericValue(digit) % 2) + 1);
        }
        return counts;
    }
}

