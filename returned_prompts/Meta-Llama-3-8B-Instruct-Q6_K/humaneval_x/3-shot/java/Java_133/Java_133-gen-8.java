        int sum = 0;
        for (double num : lst) {
            sum += Math.ceil(num) * Math.ceil(num);
        }
        return sum;
    }
}

