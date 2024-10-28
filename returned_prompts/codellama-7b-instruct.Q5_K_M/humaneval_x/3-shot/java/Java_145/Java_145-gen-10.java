        for (int i = 0; i < Math.log10(number) + 1; i++) {
            sum += Math.abs(number % 10);
            number /= 10;
        }
        return sum;
    }
}
