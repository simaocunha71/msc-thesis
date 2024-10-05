        int result = 0;
        for (int number : arr) {
            int sum = 0;
            for (int d : Integer.toString(Math.abs(number)).toCharArray()) {
                sum += d - '0';
            }
            if (sum > 0) result += 1;
        }
        return result;
    }
}

