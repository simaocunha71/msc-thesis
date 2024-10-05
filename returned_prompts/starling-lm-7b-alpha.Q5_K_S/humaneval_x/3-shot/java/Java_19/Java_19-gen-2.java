        List<String> numbers_list = Arrays.asList(numbers.split(" "));
        Collections.sort(numbers_list);
        StringBuilder result = new StringBuilder();
        for (String number : numbers_list) {
            result.append(number).append(" ");
        }
        return result.toString().trim();
    }
}

