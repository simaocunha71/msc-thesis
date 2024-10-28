    int count1 = 0;
    int count2 = 0;
    List<String> lst = new ArrayList<>();
    while(count1 < lst1.size() && count2 < lst2.size()) {
        if(lst1.get(count1).length() < lst2.get(count2).length()) {
            lst.add(lst1.get(count1));
            count1++;
        } else if(lst1.get(count1).length() > lst2.get(count2).length()) {
            lst.add(lst2.get(count2));
            count2++;
        } else {
            lst.add(lst1.get(count1));
            count1++;
            count2++;
        }
    }

    while(count1 < lst1.size()) {
        lst.add(lst1.get(count1));
        count1++;
    }
    while(count2 < lst2.size()) {
        lst.add(lst2.get(count2));
        count2++;
    }
    return lst;
    }
}
















































































































































































































































