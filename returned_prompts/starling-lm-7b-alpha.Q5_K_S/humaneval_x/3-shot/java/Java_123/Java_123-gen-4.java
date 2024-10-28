        List<Integer> result = new ArrayList<>();
        int num = n;
        while (num != 1) {
            if (num % 2 != 0) {
                result.add(num);
            }
            if (num % 2 == 0) {
                num /= 2;
            } else {
                num = 3 * num + 1;
            }
        }
        Collections.sort(result);
        return result;
    }
}

