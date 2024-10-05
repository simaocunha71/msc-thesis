        if(a instanceof Float || b instanceof Float){
            return Optional.of(Math.max(Float.parseFloat(a.toString()), Float.parseFloat(b.toString())));
        }
        else if(a instanceof Double || b instanceof Double){
            return Optional.of(Math.max(Double.parseDouble(a.toString()), Double.parseDouble(b.toString())));
        }
        else if(a instanceof Integer || b instanceof Integer){
            return Optional.of(Math.max(Integer.parseInt(a.toString()), Integer.parseInt(b.toString())));
        }
        else if(a instanceof String && b instanceof String){
            return Optional.of(Math.max(Double.parseDouble(a.toString().replaceAll(",",".")), Double.parseDouble(b.toString().replaceAll(",","."))));
        }
        else{
            return Optional.empty();
        }
    }
}

B:
class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a == null || b == null) {
            return Optional.empty();
        }
        if (a instanceof Double || b instanceof Double) {
            return Optional.of(Math.max(Double.parseDouble(a.toString()), Double.parseDouble(b.toString())));
        }
        if (a instanceof Float || b instanceof Float) {
            return Optional.of(Math.max(Float.parseFloat(a.toString()), Float.parseFloat(b.toString())));
        }
        if (a instanceof Integer || b instanceof Integer) {
            return Optional.of(Math.max(Integer.parseInt(a.toString()), Integer.parseInt(b.toString())));
        }
        if (a instanceof String && b instanceof String) {
            return Optional.of(Math.max(Double.parseDouble(a.toString().replaceAll(",", ".")), Double.parseDouble(b.toString().replaceAll(",", "."))));
        }
        return Optional.empty();
    }
}

C:
class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a == null || b == null) {
            return Optional.empty