        int sum = 0;
        for (double d : lst) {
            sum += (int) Math.ceil(d) * (int) Math.ceil(d);
        }
        return sum;
    }
}

