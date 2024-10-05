        int result = 0;
        for (Double number : lst) {
            result += Math.pow(Math.ceil(number), 2);
        }
        return result;
    }
}

