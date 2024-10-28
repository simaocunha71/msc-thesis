        if(lst.size() == 0) return 0;
        int sum1 = 0;
        int sum2 = 0;

        for(Object obj : lst) {
            if(obj instanceof Double) {
                Double d = (Double) obj;
                if(d % 2 == 0) sum1 += Math.pow(d, 2);
                else sum2 += Math.pow(d, 2);
            }
        }

        return sum1 - sum2;
    }
}






