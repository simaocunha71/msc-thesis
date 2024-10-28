        int max = Math.max(a, Math.max(b, c));
        int sum = a + b + c - max;
        return max * max == sum * sum;
    }
}

