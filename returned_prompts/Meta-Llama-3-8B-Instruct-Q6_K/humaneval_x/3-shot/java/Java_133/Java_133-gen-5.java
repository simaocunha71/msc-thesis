        int sum = 0;
        for (Double num : lst) {
            double ceil = Math.ceil(num);
            sum += (int) Math.pow(ceil, 2);
        }
        return sum;
    }
}

