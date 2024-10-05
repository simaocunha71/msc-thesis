        if (remaining >= need) {
            return Arrays.asList(number + need, remaining - need);
        } else {
            return Arrays.asList(number + remaining, 0);
        }
    }
}

