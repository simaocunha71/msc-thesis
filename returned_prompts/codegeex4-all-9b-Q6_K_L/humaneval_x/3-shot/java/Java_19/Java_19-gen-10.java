        String[] numberals = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        Map<String, Integer> number_map = new HashMap<>();
        for (int i = 0; i < numberals.length; i++) {
            number_map.put(numberals[i], i);
        }

        String[] number_array = numbers.split(" ");
        Arrays.sort(number_array, (a, b) -> number_map.get(a) - number_map.get(b));
        return String.join(" ", number_array);
    }
}

