        if (remaining < need) return Arrays.asList(number + remaining, 0);
        return Arrays.asList(number + need, remaining - need);
    }
}

