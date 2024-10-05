        int sum = 0;
        for (double num : lst) {
            sum += (int)Math.ceil(num) * (int)Math.ceil(num);
        }
        return sum;
    }
}

