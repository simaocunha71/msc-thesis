        Map<Integer, Integer> freq_map = new HashMap<>();
        for  (int num  : lst)  {
            freq_map.put(num, freq_map.getOrDefault(num, 0) + 1);
        }

        for  (int i = lst.size() - 1; i > 0; i--)  {
            if  (freq_map.getOrDefault(i, 0) >= i)  return i;
        }
        return -1;
     }
}

