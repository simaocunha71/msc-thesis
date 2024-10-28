        List<Integer> list = new ArrayList<Integer>();
        for(int i = 0; i < l.size(); i++)
        {
            if(i % 3 == 0)
            {
                list.add(l.get(i));
                continue;
            }
            list.add(l.get(i));
        }
        Collections.sort(list);
        return list;
    }
}
