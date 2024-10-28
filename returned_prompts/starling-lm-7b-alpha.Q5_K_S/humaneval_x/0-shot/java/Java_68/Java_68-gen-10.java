        List<Integer> result = null;
        List<Integer> evenList = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0) {
                evenList.add(i);
            }
        }
        if (evenList.size() > 0) {
            result = new ArrayList<>();
            result.add(arr.get(evenList.get(0)));
            result.add(evenList.get(0));
        }
        if (evenList.size() > 1) {
            for (int i = 1; i < evenList.size(); i++) {
                if (arr.get(evenList.get(i)) < arr.get(evenList.get(i - 1))) {
                    result = new ArrayList<>();
                    result.add(arr.get(evenList.get(i)));
                    result.add(evenList.get(i));
                    continue A;
                }
            }
        }
        return result;
    }
}




/*























*/
















































*/
```