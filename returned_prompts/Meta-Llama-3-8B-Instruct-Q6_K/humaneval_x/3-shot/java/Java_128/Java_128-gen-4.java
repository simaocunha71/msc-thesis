        if (arr.isEmpty()) {
            return Optional.empty();
        }

        int productSigns = 1;
        int sumMagnitudes = 0;

        for (int num : arr) {
            if (num != 0) {
                productSigns *= Math.signum(num);
            }
            sumMagnitudes += Math.abs(num);
        }

        return Optional.of(sumMagnitudes * productSigns);
    }
}

