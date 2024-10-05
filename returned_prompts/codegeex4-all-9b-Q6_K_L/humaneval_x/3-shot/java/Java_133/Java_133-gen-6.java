        int result = 0;
        for (double x : lst) {
            result += (int)Math.ceil(x) * (int)Math.ceil(x);
        }
        return result;
    }
}

