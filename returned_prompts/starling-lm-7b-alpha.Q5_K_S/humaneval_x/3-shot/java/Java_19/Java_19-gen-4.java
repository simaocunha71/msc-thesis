        List<String> number_list = new ArrayList<>(Arrays.asList("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"));
        Map<String, Integer> number_map = new HashMap<>();
        for (int i = 0; i < number_list.size(); i++) {
            number_map.put(number_list.get(i), i);
        }

        List<String> result = new ArrayList<>();
        String[] tokens = numbers.split(" ");
        for (String token : tokens) {
            int index = number_map.get(token);
            result.add(number_list.get(index));
        }

        Collections.sort(result);

        return String.join(" ", result);
    }
}

