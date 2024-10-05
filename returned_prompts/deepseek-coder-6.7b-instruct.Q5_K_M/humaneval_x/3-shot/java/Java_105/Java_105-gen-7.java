        List<String> names = new ArrayList<String>(Arrays.asList("", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"));
        List<Integer> filtered = new ArrayList<Integer>();
        for(int num : arr) {
            if(num > 0 && num < 10) {
                filtered.add(num);
            }
        }
        Collections.sort(filtered, Collections.reverseOrder());
        List<String> result = new ArrayList<String>();
        for(int num : filtered) {
            result.add(names.get(num));
        }
        return result;
    }
}

