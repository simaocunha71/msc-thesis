        List<Integer> result = new ArrayList<>();
        result.add(0);
        result.add(0);

        while (num > 0) {
            if (num % 2 == 0) result.set(0, result.get(0) + 1);
            else result.set(1, result.get(1) + 1);
            num /= 10;
        }
        return result;
    }
}

