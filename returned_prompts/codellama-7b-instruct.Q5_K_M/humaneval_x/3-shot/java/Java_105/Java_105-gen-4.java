        List<String> result = new ArrayList<>();

        if (arr.size() == 0) return result;

        // Sort the array and reverse it
        arr.sort(null);
        arr.reverse();

        // Fill the result array
        for (Integer i : arr) {
            if (i > 0 && i < 10) {
                result.add(getNumber(i));
            }
        }
        return result;
    }

    public String getNumber(int number) {
        switch (number) {
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
                return "Unknown";
        }
    }
}

