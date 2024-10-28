        List<String> list = new ArrayList<>();
        String[] arr = numbers.split(" ");
        for (String n : arr) {
            switch (n) {
                case "zero":
                    list.add("0");
                    break;
                case "one":
                    list.add("1");
                    break;
                case "two":
                    list.add("2");
                    break;
                case "three":
                    list.add("3");
                    break;
                case "four":
                    list.add("4");
                    break;
                case "five":
                    list.add("5");
                    break;
                case "six":
                    list.add("6");
                    break;
                case "seven":
                    list.add("7");
                    break;
                case "eight":
                    list.add("8");
                    break;
                case "nine":
                    list.add("9");
                    break;
            }
        }
        Collections.sort(list);
        return String.join(" ", list);
    }
}









































































































































































































































