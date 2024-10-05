        List<Integer> result = new ArrayList<>();
        int max_so_far = numbers.get(0);

        for (int n : numbers) {
            if (n > max_so_far) max_so_far = n;
            result.add(max_so_far);
        }
        return result;
    }
}

