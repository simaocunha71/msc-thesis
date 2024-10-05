    List<Integer> arr1 = new ArrayList<>();
    List<String> arr2 = new ArrayList<>();

    for (int i = 0; i < arr.size(); i++) {
        if (arr.get(i) >= 1 && arr.get(i) <= 9) {
            arr1.add(arr.get(i));
        }
    }

    Collections.sort(arr1);
    Collections.reverse(arr1);

    for (int i = 0; i < arr1.size(); i++) {
        switch (arr1.get(i)) {
            case 1:
                arr2.add("One");
                break;
            case 2:
                arr2.add("Two");
                break;
            case 3:
                arr2.add("Three");
                break;
            case 4:
                arr2.add("Four");
                break;
            case 5:
                arr2.add("Five");
                break;
            case 6:
                arr2.add("Six");
                break;
            case 7:
                arr2.add("Seven");
                break;
            case 8:
                arr2.add("Eight");
                break;
            case 9:
                arr2.add("Nine");
                break;
        }
    }

    return arr2;
}
}



Ans:
In the given program, the function byLength takes a List of Integers as input and returns a List of Strings as output. The purpose of this function is to sort the integers between 1 and 9 (inclusive), reverse the resulting array, and then replace each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

To achieve this, the function first creates two empty Lists: arr1 to store the integers between 1 and 9 (inclusive), and arr2 to store the corresponding names as Strings. It then iterates through the input array and checks if each