        List<Integer> ceiled_list = new ArrayList<>();
        for (double number : lst) {
            ceiled_list.add((int) Math.ceil(number));
        }
        int result = 0;
        for (int number : ceiled_list) {
            result += number * number;
        }
        return result;
    }
}

