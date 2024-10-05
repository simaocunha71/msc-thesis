        int result = 0;
        for (Object number : lst) {
            if (number instanceof Integer && ((Integer) number) % 2 == 1) {
                result += ((Integer) number) * ((Integer) number);
            }
        }
        return result;
    }
}

