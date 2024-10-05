        int sum = 0;
        for (double num : lst) {
            int ceil = (int) Math.ceil(num);
            sum += Math.pow(ceil, 2);
        }
        return sum;
    }
}

