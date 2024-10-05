        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            if (num % 2 == 0) continue;
            int num_copy = num;
            while (num_copy > 0) {
                int digit = num_copy % 10;
                if (digit % 2 == 0) {
                    num_copy /= 10;
                } else {
                    break;
                }
            }
            if (num_copy == 0) result.add(num);
        }
        Collections.sort(result);
        return result;
    }
}

