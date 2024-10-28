        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < x.size(); i++) {
            int num = x.get(i);
            boolean is_unique = true;
            while (num > 0) {
                int digit = num % 10;
                if (digit % 2 == 0) {
                    is_unique = false;
                    break;
                }
                num = num / 10;
            }
            if (is_unique) {
                result.add(x.get(i));
            }
        }
        Collections.sort(result);
        return result;
    }
}

