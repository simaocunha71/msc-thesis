        int eaten = Math.min(Math.min(need, remaining), need - number);
        int left = remaining - eaten;

        return Arrays.asList(number + eaten, left);
    }
}

