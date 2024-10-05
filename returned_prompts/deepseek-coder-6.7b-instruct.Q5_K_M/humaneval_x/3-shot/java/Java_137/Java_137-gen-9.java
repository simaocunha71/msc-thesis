        if  (a instanceof Integer && b instanceof Integer) 
            return (Integer)a > (Integer)b ? Optional.of(a) : Optional.empty();
        else if  (a instanceof Double && b instanceof Double) 
            return (Double)a > (Double)b ? Optional.of(a) : Optional.empty();
        else if  (a instanceof String && b instanceof String) 
            return Double.parseDouble((String)a) > Double.parseDouble((String)b) ? Optional.of(a) : Optional.empty();
        else if  (a instanceof String && b instanceof Double) 
            return Double.parseDouble((String)a) > (Double)b ? Optional.of(a) : Optional.empty();
        else if  (a instanceof Double && b instanceof Integer) 
            return (Double)a > (Integer)b ? Optional.of(a) : Optional.empty();
        else if  (a instanceof String && b instanceof Integer) 
            return Double.parseDouble((String)a) > (Integer)b ? Optional.of(a) : Optional.empty();
        else if  (a instanceof Integer && b instanceof String) 
            return (Integer)a > Double.parseDouble((String)b) ? Optional.of(b) : Optional.empty();
        else if  (a instanceof Double && b instanceof String) 
            return (Double)a > Double.parseDouble((String)b) ? Optional.of(b) : Optional.empty();
        else 
            return Optional.empty();
      }
}

