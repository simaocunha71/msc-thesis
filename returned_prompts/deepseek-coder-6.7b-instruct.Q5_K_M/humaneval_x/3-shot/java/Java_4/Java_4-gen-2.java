        double mean 0.0;
        for (double number  : numbers)  {
            mean += number;
        }
        mean /= numbers.size();

        double mad 0.0;
        for  (double number  : numbers)  {
            mad += Math.abs(number  - mean);
        }
        return mad / numbers.size();
     }
}

