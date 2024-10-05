        List<String> number_strings = Arrays.asList(numbers.split(" "));
        Collections.sort(number_strings);

        StringBuilder result = new StringBuilder();
        for (String number_string : number_strings) {
            result.append(number_string).append(" ");
        }
        return result.toString().trim();
    }
}

