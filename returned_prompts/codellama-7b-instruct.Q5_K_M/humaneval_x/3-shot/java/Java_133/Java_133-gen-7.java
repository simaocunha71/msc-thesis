        int result = 0;
        for (Double d : lst) {
            result += Math.pow(Math.ceil(d), 2);
        }
        return result;
    }
}

