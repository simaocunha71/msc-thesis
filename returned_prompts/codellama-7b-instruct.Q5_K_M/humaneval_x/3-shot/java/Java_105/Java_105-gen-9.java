        List<String> result = new ArrayList<>();
        arr.sort(Integer::compareTo);
        Collections.reverse(arr);

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) >= 1 && arr.get(i) <= 9) {
                result.add(i, name(arr.get(i)));
            }
        }
        return result;
    }

    private String name(int number) {
        switch (number) {
            case 1: return "One";
            case 2: return "Two";
            case 3: return "Three";
            case 4: return "Four";
            case 5: return "Five";
            case 6: return "Six";
            case 7: return "Seven";
            case 8: return "Eight";
            case 9: return "Nine";
        }
        return "";
    }
}

