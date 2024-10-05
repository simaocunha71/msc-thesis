        int sum = 0;
        for (double elem : lst) {
            sum += (int) Math.pow(Math.ceil(elem), 2);
        }
        return sum;
    }
}

