        int sum = 0;
        for (double x : lst) {
            sum += (int)Math.ceil(x) * (int)Math.ceil(x);
        }
        return sum;
    }
}

