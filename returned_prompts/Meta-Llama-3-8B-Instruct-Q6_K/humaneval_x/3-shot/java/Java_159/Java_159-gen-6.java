        int eaten = number + need - remaining;
        return Arrays.asList(eaten, remaining - (eaten - need));
    }
}

