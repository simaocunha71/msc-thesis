import java.util.*;

class Solution {
    public List<Integer> uniqueDigits(List<Integer> x) {
        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < x.size(); i++){
            if(x.get(i)%2 == 0){
                continue;
            }
            else{
                result.add(x.get(i));
            }
        }
        return result;
    }
}
