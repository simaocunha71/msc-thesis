        List<Integer> result = new ArrayList<>();
        int current_num = a;

        while (current_num <= b) {
            if (current_num % 2 == 0) {
                result.add(current_num);
            }
            current_num += 1;
        }

        return result;
    }
}

