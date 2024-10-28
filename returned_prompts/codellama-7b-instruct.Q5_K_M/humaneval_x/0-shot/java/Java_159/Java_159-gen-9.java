        List<Integer> result = new ArrayList<>();

        int total = number + need;
        result.add(total);

        if (remaining >= total) {
            result.add(remaining - total);
        } else {
            result.add(0);
        }

        return result;
    }
}
