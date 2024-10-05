        List<String> filtered = new ArrayList<String>();
        for(String str : strings){
            if(str.contains(substring))
                filtered.add(str);
        }
        return filtered;
    }
}

The provided code is correct. It creates a new list called filtered and iterates over the input list of strings. If a string from the list contains the substring, it is added to the filtered list. Finally, the filtered list is returned.

The time complexity of this code is O(