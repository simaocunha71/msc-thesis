        Collections.sort(arr);
        Collections.reverse(arr);
        List<String> result = new ArrayList<>();

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) >= 1 && arr.get(i) <= 9) {
                result.add(byLengthSwitchCase(arr.get(i)));
            }
        }
        return result;
    }

    public String byLengthSwitchCase(int i) {
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
        return "Unknown";
    }
}

