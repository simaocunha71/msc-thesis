        List<Integer> result = new ArrayList<>();
        result.add(n);

        for (int i = 1; n % 2 == 0; n++) {
            result.add(n);
            n++;
        }

        for (int i = 1; n % 2 != 0; n++) {
            result.add(n);
            n++;
        }

        return result;
    }
}

