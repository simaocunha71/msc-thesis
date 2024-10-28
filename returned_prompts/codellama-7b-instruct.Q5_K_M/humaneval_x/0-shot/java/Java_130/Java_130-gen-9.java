        List<Integer> result = new ArrayList<>();
        int tri1 = 1;
        int tri2 = 3;
        int tri3 = 2;

        result.add(tri1);
        result.add(tri2);
        result.add(tri3);

        for (int i = 3; i <= n; i++) {
            if (i % 2 == 0) {
                result.add(tri1 + i / 2);
            } else {
                result.add(tri1 + tri2 + tri3);
            }
        }

        return result;
    }
}


