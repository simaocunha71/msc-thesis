        double sum = 0;
        double mean = 0;
        double mad = 0;

        for(double num : numbers){
            sum += num;
        }

        mean = sum / numbers.size();

        for(double num : numbers){
            mad += Math.abs(num - mean);
        }

        return mad / numbers.size();
    }
}

In this code, we first calculate the mean of the input numbers. Then for each number in the dataset, we calculate its absolute deviation from the mean, and sum up these absolute deviations. Finally, we divide the sum by the size of the dataset to get the mean absolute deviation.
*/


