        int oddLst1 = 0, evenLst2 = 0;
        for(int i : lst1)
            if(i % 2 != 0) oddLst1++;
        for(int i : lst2)
            if(i % 2 == 0) evenLst2++;
        return oddLst1 > evenLst2 ? "NO" : "YES";
     }
}

