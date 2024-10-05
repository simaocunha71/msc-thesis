        double sum = 0;
        double mean 
        = numbers.stream().mapToDouble(Double::doubleValue).sum() / numbers.size();
        
        for(double num : numbers) {
            sum += Math.abs(num - mean);
        }

        return sum / numbers.size();
     }
}

