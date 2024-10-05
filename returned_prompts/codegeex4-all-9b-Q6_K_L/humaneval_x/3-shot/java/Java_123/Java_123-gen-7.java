        List<Integer> result = new ArrayList<>();
        int current = n;

        while (current != 1) {
            if (current % 2 != 0) {
                result.add(current);
            }
            current = current / 2 + current % 2 * 3;
        }
        result.add(1);
        Collections.sort(result);
        return result;

    }
}

