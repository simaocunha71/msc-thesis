        int total_water = 0;
        for (List<Integer> row  : grid)  {
            for  (int well  : row)  {
                total_water += well;
            }
        }
        return (total_water + capacity - 1) / capacity;
     }
}

