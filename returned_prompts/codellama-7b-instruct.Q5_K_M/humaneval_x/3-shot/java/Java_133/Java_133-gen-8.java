        int result = 0;
        for (double d : lst) {
            result += Math.pow(Math.ceil(d), 2);
        }
        return result;
    }
}

