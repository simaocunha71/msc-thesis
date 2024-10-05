        Collections.sort(arr);
        Collections.reverse(arr);
        List<String> result = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            result.add(oneToNine(arr.get(i)));
        }
        return result;
    }

    public String oneToNine(int i) {
        switch (i) {
            case 1: return "One";
            case 2: return "Two";
            case 3: return "Three";
            case 4: return "Four";
            case 5: return "Five";
            case 6: return "Six";
            case 7: return "Seven";
            case 8: return "Eight";
            case 9: return "Nine";
            default: return "";
        }
    }

    public List<String> byLength(String[] arr) {
        List<Integer> arr_int = new ArrayList<>();
        for (String s : arr) {
            arr_int.add(Integer.parseInt(s));
        }
        return byLength(arr_int);
    }
}

