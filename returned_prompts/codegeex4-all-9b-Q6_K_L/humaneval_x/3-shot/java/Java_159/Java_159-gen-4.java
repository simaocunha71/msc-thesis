        int eaten = need;
        if (remaining < need) {
            eaten = remaining;
        }
        int left = remaining - eaten;
        return Arrays.asList(number + eaten, left);
    }
}

