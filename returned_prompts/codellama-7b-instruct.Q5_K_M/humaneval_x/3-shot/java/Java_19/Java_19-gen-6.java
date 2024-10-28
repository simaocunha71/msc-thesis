        List<Integer> int_list = new ArrayList<>();
        for (String number : numbers.split(" ")) {
            int_list.add(Integer.parseInt(number));
        }
        Collections.sort(int_list);

        StringBuilder result = new StringBuilder();
        for (int number : int_list) {
            result.append(number).append(" ");
        }
        return result.toString().trim();
    }
}

