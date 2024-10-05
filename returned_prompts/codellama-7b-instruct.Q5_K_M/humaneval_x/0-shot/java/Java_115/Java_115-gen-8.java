        // 1. find the longest well in the grid
        // 2. find the number of wells that are greater than the longest well
        // 3. calculate the number of times you need to lower the bucket

        int longest_well_length = 0;
        int number_of_wells_larger_than_longest_well = 0;

        for (int i = 0; i < grid.size(); i++) {
            int well_length = grid.get(i).size();
            if (well_length > longest_well_length) {
                longest_well_length = well_length;
            } else if (well_length < longest_well_length) {
                number_of_wells_larger_than_longest_well += 1;
            }
        }

        // calculate the number of times you need to lower the bucket
        int number_of_times_to_lower_bucket = longest_well_length - number_of_wells_larger_than_longest_well;

        return number_of_times_to_lower_bucket;
    }
}
