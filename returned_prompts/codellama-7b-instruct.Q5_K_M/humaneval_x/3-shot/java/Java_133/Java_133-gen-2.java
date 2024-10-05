        int result = 0;
        for (Double d : lst) {
            int rounded = (int) Math.ceil(d);
            result += (rounded * rounded);
        }
        return result;
    }
}

