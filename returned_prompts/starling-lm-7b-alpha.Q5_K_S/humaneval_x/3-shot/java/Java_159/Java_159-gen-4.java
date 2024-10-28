        int total = need - number + remaining;
        int left = remaining - (need - number);

        return Arrays.asList(total, left);
    }
}

