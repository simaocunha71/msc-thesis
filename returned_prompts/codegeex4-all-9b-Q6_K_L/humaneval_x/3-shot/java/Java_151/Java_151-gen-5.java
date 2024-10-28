        int result = 0;

        for (Object o : lst) {
            int num = (int) o;
            if (num % 2 == 1 && num >= 0) {
                result += num * num;
            }
        }
        return result;
    }
}

