        List<String> res = new ArrayList<>();
        if (arr.size() == 0) {
            return res;
        }

        Collections.sort(arr, Collections.reverseOrder());
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) <= 0 || arr.get(i) > 9) {
                continue;
            }
            res.add(name(arr.get(i)));
        }

        return res;
    }

    private String name(int i) {
        switch (i) {
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
        }
        return "";
    }
}











































































































































































































































