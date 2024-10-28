        List<Integer> result = new ArrayList<>();
        for (Integer num : x) {
            if (num % 2 == 0) continue;
            boolean valid = true;
            for (int d = 1; d <= num; d *= 10) {
                if (d * num % 10 % 2 == 0) {
                    valid = false;
                }
            }
            if (valid) result.add(num);
        }
        Collections.sort(result);
        return result;
    }
}


