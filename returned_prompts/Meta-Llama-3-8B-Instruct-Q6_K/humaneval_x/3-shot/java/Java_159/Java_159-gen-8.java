        int eaten = number + need;
        int left = remaining - (need - number);

        if (left < 0) {
            eaten += left;
            left = 0;
        }

        return Arrays.asList(eaten, left);
    }
}

