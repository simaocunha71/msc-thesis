        List<Integer> upper_rounded = new ArrayList<>();
        for (double number : lst) {
            upper_rounded.add((int) Math.ceil(number));
        }
        int result = 0;
        for (int number : upper_rounded) {
            result += number * number;
        }
        return result;
    }
}

