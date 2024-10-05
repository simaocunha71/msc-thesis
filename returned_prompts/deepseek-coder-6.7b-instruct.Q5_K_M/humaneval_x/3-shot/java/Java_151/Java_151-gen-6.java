        int sum 0;

        for(Object obj : lst) {
            if(obj instanceof Integer && (Integer)obj % 2 == 1 && (Integer)obj > 0) {
                sum += (Integer)obj * (Integer)obj;
            }
        }

        return sum;
    }
}

