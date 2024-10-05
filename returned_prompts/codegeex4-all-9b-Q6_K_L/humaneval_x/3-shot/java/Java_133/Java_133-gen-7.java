        int sum = 0;
        for (double n : lst) {
            sum += (int)Math.ceil(n) * (int)Math.ceil(n);
        }
        return sum;
    }
}

