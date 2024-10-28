        int result = 0;

        for (Double n : lst) {
            int rounded_number = (int) Math.ceil(n);
            result += rounded_number * rounded_number;
        }
        return result;
    }
}

