        if(a instanceof Integer && b instanceof Integer){
            if((Integer)a > (Integer)b){
                return Optional.of(a);
            }else if((Integer)a < (Integer)b){
                return Optional.of(b);
            }
        }

        if(a instanceof Float && b instanceof Float){
            if((Float)a > (Float)b){
                return Optional.of(a);
            }else if((Float)a < (Float)b){
                return Optional.of(b);
            }
        }

        if(a instanceof String && b instanceof String){
            if(Float.parseFloat((String)a) > Float.parseFloat((String)b)){
                return Optional.of(a);
            }else if(Float.parseFloat((String)a) < Float.parseFloat((String)b)){
                return Optional.of(b);
            }
        }

        if(a instanceof Integer && b instanceof Float){
            if((Integer)a > Float.parseFloat((String)b)){
                return Optional.of(a);
            }else if((Integer)a < Float.parseFloat((String)b)){
                return Optional.of(b);
            }
        }

        if(a instanceof Float && b instanceof Integer){
            if((Float)a > (Integer)b){
                return Optional.of(a);
            }else if((Float)a < (Integer)b){
                return Optional.of(b);
            }
        }

        if(a instanceof String && b instanceof Float){
            if(Float.parseFloat((String)a) > (Float)b){
                return Optional.of(a);
            }else if(Float.parseFloat((String)a) < (Float)b){
                return Optional.of(b);
            }
        }

        if(a instanceof Float && b instanceof String){
            if((Float)a > Float.parseFloat((String)b)){
                return Optional.of(a);
            }else if((Float)a < Float.parseFloat((String)b)){
                return Optional.of(b);
            }
       