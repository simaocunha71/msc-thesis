    List<Integer> list = new ArrayList<Integer>();
    List<String> res = new ArrayList<String>();
    for(int i=0;i<arr.size();i++) {
        if(arr.get(i) >= 1 && arr.get(i) <= 9) {
            list.add(arr.get(i));
        }
    }
    Collections.sort(list);
    Collections.reverse(list);
    for(int i:list) {
        if(i == 1) {
            res.add("One");
        } else if(i == 2) {
            res.add("Two");
        } else if(i == 3) {
            res.add("Three");
        } else if(i == 4) {
            res.add("Four");
        } else if(i == 5) {
            res.add("Five");
        } else if(i == 6) {
            res.add("Six");
        } else if(i == 7) {
            res.add("Seven");
        } else if(i == 8) {
            res.add("Eight");
        } else if(i == 9) {
            res.add("Nine");
        }
    }
    return res;
}
}








































































































































































































