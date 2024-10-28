        List<String> list = new ArrayList<>();
        if (arr.isEmpty()) return list;
        arr = arr.stream().filter(x -> x >= 1 && x <= 9).sorted().collect(Collectors.toList());
        if (arr.isEmpty()) return list;
        list = arr.stream().map(x -> {
            switch (x) {
                case 1:
                    return "One";
                case 2:
                    return "Two";
                case 3:
                    return "Three";
                case 4:
                    return "Four";
                case 5:
                    return "Five";
                case 6:
                    return "Six";
                case 7:
                    return "Seven";
                case 8:
                    return "Eight";
                case 9:
                    return "Nine";
                default:
                    return "";
            }
        }).collect(Collectors.toList());
        Collections.reverse(list);
        return list;
    }
}
