        int sum = 0;
        for (double d : lst) {
            int ceil = (int) Math.ceil(d);
            sum += Math.pow(ceil, 2);
        }
        return sum;
    }
}

