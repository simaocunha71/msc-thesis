        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            result.add(i % 2 == 0 ? i + 1 : i + 2);
        }
        return result;
    }
}


