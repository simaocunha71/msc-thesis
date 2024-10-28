        int total_water 0;
        for (List<Integer> row  : grid)  total_water += sum(row);
        return (total_water  +  capacity  - 1)  //  capacity;
    }
}

