        List<Integer> result = new ArrayList<>();
        int stones = n;

        while (stones > 0) {
            if (stones % 2 == 1) {
                result.add(0, stones);
                stones -= 1;
            } else {
                result.add(0, stones);
                stones -= 2;
            }
        }
        return result;
    }
}

