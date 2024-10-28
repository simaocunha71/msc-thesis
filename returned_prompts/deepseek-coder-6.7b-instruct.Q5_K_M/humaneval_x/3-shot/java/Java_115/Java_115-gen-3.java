        int total_water = 0;
        for  (List<Integer> row  : grid)  {
            for  (int cell  : row)  {
                total_water += cell;
             }
         }
        return (int)Math.ceil((double)total_water / capacity);
     }
}

