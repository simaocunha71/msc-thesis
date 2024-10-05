        int min = 0;
        int max = arr.size() - 1;
        int sum = 0;
        while (min <= max) {
            if (arr.get(min) != arr.get(max)) {
                min++;
                max--;
                sum++;
            } else {
                min++;
                max--;
            }
        }
        return sum;
    }
}
