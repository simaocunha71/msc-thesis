        int sum = 0;
        for (Double number : lst) {
            sum += Math.pow(Math.ceil(number), 2);
        }
        return sum;
    }
}

