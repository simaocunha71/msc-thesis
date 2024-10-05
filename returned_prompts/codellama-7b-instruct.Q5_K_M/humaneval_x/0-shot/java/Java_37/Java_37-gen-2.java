        List<Integer> l1 = new ArrayList<Integer>();
        List<Integer> l2 = new ArrayList<Integer>();
        for(int i=0; i<l.size(); i++)
        {
            if(i%2==0)
            {
                l1.add(l.get(i));
            }
            else
            {
                l2.add(l.get(i));
            }
        }
        l2.sort(Integer::compare);
        for(int i=0; i<l1.size(); i++)
        {
            l1.set(i, l1.get(i)+l2.get(i));
        }
        return l1;
    }
}
