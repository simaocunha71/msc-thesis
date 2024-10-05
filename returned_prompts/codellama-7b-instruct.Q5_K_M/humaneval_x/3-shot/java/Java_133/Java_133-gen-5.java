        int result = 0;

        for (double value : lst) {
            result += (int) Math.pow(Math.ceil(value), 2);
        }
        return result;
    }
}

