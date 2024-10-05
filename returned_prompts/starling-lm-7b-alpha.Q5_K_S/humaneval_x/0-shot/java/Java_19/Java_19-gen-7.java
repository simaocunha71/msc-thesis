    List<String> list = new ArrayList<>();
    String[] nums = numbers.split(" ");
    for (String n : nums) {
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

    StringBuilder sb = new StringBuilder();
    for (String s : list) {
        switch (s) {
            case "0":
                sb.append("zero ");
                break;
            case "1":
                sb.append("one ");
                break;
            case "2":
                sb.append("two ");
                break;
            case "3":
                sb.append("three ");
                break;
            case "4":
                sb.append("four ");
                break;
            case "5":
                sb.append("five ");
                break;
            case "6":
                sb.append("six ");
                break;
            case "7":
                sb.append("seven ");
                break;
            case "8":
                sb.append("eight ");
                break;
            case "9":
                sb.append("nine ");
                break;
        }
    }
    return sb.toString();
    }
}











