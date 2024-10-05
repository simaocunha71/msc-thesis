        int result = 0;
        for (double n : lst) {
            result += (int) Math.pow(Math.ceil(n), 2.0);
        }
        return result;
    }
}

