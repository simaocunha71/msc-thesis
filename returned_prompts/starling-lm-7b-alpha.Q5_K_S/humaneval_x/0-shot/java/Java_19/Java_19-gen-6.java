
        List<String> digits = new ArrayList<>();
        for (String s : numbers.split(" ")) {
            switch (s) {
                case "zero":
                    digits.add("0");
                    break;
                case "one":
                    digits.add("1");
                    break;
                case "two":
                    digits.add("2");
                    break;
                case "three":
                    digits.add("3");
                    break;
                case "four":
                    digits.add("4");
                    break;
                case "five":
                    digits.add("5");
                    break;
                case "six":
                    digits.add("6");
                    break;
                case "seven":
                    digits.add("7");
                    break;
                case "eight":
                    digits.add("8");
                    break;
                case "nine":
                    digits.add("9");
                    break;
            }
        }
        Collections.sort(digits);

        StringBuffer sb = new StringBuffer();
        for (String s : digits) {
            switch (s) {
                case "0":
                    sb.append("zero");
                    break;
                case "1":
                    sb.append("one");
                    break;
                case "2":
                    sb.append("two");
                    break;
                case "3":
                    sb.append("three");
                    break;
                case "4":
                    sb.append("four");
                    break;
                case "5":
                    sb.append("five");
                    break;
                case "6":
                    sb.append("six");
                    break;
                case "7":
                    sb.append("seven");
                    break;
                case "8":
                    sb.append("eight");
                    break;
                case "9":
                    sb.append("nine");
                    break;
            }