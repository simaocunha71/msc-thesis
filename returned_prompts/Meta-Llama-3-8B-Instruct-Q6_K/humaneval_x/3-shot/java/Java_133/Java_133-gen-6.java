        int sum = 0;
        for (Double num : lst) {
            double ceiling = Math.ceil(num);
            sum += (int) Math.pow(ceiling, 2);
        }
        return sum;
    }
}

