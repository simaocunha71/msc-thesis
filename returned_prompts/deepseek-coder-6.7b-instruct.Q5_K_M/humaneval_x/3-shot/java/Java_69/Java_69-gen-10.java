        Map<Integer, Integer> counts = new HashMap<>();

        for  (int num : lst)  {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }

        for  (int num : counts.keySet())  {
            if  (num <= lst.size() && counts.get(num) >= num)  {
                return num;
            }
        }
        return -1;
    }
}

