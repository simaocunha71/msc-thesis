        int sum = 0;
        for (Double num : lst) {
            sum += Math.ceil(num) * Math.ceil(num);
        }
        return sum;
    }
}

