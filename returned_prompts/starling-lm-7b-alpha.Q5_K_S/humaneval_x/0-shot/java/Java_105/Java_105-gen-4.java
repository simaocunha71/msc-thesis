    List<String> strList = new ArrayList<>();
    List<Integer> intList = new ArrayList<>(arr);

    Collections.sort(intList);
    Collections.reverse(intList);

    for (Integer i : intList) {
        switch (i) {
            case 1:
                strList.add("One");
                break;
            case 2:
                strList.add("Two");
                break;
            case 3:
                strList.add("Three");
                break;
            case 4:
                strList.add("Four");
                break;
            case 5:
                strList.add("Five");
                break;
            case 6:
                strList.add("Six");
                break;
            case 7:
                strList.add("Seven");
                break;
            case 8:
                strList.add("Eight");
                break;
            case 9:
                strList.add("Nine");
                break;
            default:
                strList.add("");
                break;
        }
    }
    return strList;
}
}




























































































































































































































