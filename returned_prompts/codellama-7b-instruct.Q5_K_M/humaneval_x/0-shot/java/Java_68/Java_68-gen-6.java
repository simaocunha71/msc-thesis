        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0) {
                return Arrays.asList(arr.get(i), i);
            }
        }
        return new ArrayList<>();
    }
}

