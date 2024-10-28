        List<Integer> result = new ArrayList<>();
        result.add(1);
        result.add(3);
        result.add(2);

        if (n > 2) {

            for (int i = 3; i <= n; i++) {
                if (i % 2 == 0)
                    result.add((int) Math.ceil((i / 2.0)));
                else
                    result.add(result.get(i - 1) + result.get(i - 2) + result.get(i + 1));
            }
        }
        return result;
    }
}

