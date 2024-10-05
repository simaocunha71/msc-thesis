        int max_length = Math.max(Math.max(a, b), c);
        int min_length = Math.min(Math.min(a, b), c);
        int middle_length = a + b + c - max_length - min_length;

        return min_length * min_length + middle_length * middle_length == max_length * max_length;
    }
}

