        int sum = 0;
        int negativeCount = 0;
        for (int i : arr) {
            if (i == 0) continue;
            if (i < 0) {
                i = -i;
                negativeCount += 1;
            }
            sum += i;
        }
        if (negativeCount % 2 == 0) {
            return Optional.of(sum);
        } else {
            return Optional.of(-sum);
        }
    }
}

