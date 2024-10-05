        String[] numberals = numbers.split(" ");
        Arrays.sort(numberals, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return getNumericalValue(o1) - getNumericalValue(o2);
            }
        });
        return String.join(" ", numberals);
    }

    private int getNumericalValue(String numberal) {
        switch (numberal) {
            case "zero":
                return 0;
            case "one":
                return 1;
            case "two":
                return 2;
            case "three":
                return 3;
            case "four":
                return 4;
            case "five":
                return 5;
            case "six":
                return 6;
            case "seven":
                return 7;
            case "eight":
                return 8;
            case "nine":
                return 9;
            default:
                throw new IllegalArgumentException("Invalid numberal: " + numberal);
        }
    }
}

