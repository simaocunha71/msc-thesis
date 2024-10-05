        List<Integer> result = new ArrayList<>();
        result.add(3);
        result.add(1);
        result.add(2);
        result.add(8);

        if (n == 0) return result;

        int count = 0;

        while (count < n) {
            int temp = result.get(result.size() - 1) + result.get(result.size() - 2) + result.get(result.size() - 3);
            result.add(temp);
            count += 1;
        }
        return result;
    }
}

