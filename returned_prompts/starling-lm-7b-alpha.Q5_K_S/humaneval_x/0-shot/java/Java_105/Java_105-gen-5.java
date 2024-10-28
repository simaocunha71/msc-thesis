    if(arr.isEmpty()){
        return new ArrayList<>();
    }

    List<Integer> sortArr = new ArrayList<>();
    sortArr.addAll(arr);
    Collections.sort(sortArr);
    Collections.reverse(sortArr);

    List<String> arrName = new ArrayList<>();
    for(int i = 0; i < sortArr.size(); i++){
        switch(sortArr.get(i)){
            case 1:
                arrName.add("One");
                break;
            case 2:
                arrName.add("Two");
                break;
            case 3:
                arrName.add("Three");
                break;
            case 4:
                arrName.add("Four");
                break;
            case 5:
                arrName.add("Five");
                break;
            case 6:
                arrName.add("Six");
                break;
            case 7:
                arrName.add("Seven");
                break;
            case 8:
                arrName.add("Eight");
                break;
            case 9:
                arrName.add("Nine");
                break;
            default:
                continue A;
        }
    }
    return arrName;
}
}





























































































































































































