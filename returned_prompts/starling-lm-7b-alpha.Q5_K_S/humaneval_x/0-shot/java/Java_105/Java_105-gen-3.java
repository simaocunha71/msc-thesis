    List<Integer> arr1 = new ArrayList<>();
    List<Integer> arr2 = new ArrayList<>();
    List<Integer> arr3 = new ArrayList<>();

    for (int i = 0; i < arr.size(); i++) {
        if (arr.get(i) >= 1 && arr.get(i) <= 9) {
            arr1.add(arr.get(i));
        } else {
            arr2.add(arr.get(i));
        }
    }

    Collections.sort(arr1);
    Collections.sort(arr2);

    for (int i = arr.size() - 1; i >= 0; i--) {
        if (arr.get(i) >= 1 && arr.get(i) <= 9) {
            arr3.add(arr.get(i));
        } else {
            arr3.add(arr.get(i));
        }
    }

    Collections.reverse(arr3);

    List<String> res = new ArrayList<>();
    for (int i = 0; i < arr3.size(); i++) {
        switch (arr3.get(i)) {
            case 1:
                res.add("One");
                break;
            case 2:
                res.add("Two");
                break;
            case 3:
                res.add("Three");
                break;
            case 4:
                res.add("Four");
                break;
            case 5:
                res.add("Five");
                break;
            case 6:
                res.add("Six");
                break;
            case 7:
                res.add("Seven");
                break;
            case 8:
                res.add("Eight");
                break;
            case 9:
                res.add("Nine");
                break;
        }
    }

    return res;
}
}

































