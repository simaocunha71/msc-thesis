        if (number == 0) return 1;
        if (number < 0) number = -number;
        int count = 0;
        while (number > 0) {
            count++;
            number /= 10;
        }
        return count;
    }
}

