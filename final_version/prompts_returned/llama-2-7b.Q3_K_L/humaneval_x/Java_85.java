import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a non-empty list of integers lst. add the even elements that are at odd indices..

    Examples:
        add(Arrays.asList(4, 2, 6, 7)) ==> 2
     */
    public int add(List<Integer> lst) {
        
        List<Integer> even = new ArrayList<>();
        Set<Integer> prime = new HashSet<>();
        for(int i=0;i<=lst.size();i++){
            if(!prime.contains(lst.get(i))){
                if((i%2) == 1 && lst.get(i) % 2 == 0 ) {
                    even.add(lst.get(i));
                    
                }else{
                    prime.add(lst.get(i));
                }
            }
        }
        
        int max = (even.size() - 1) + lst.size();
        while(!even.isEmpty()) {
            
            for (int i = even.size()-2; i >=0 ; i--){
                
                if(lst.get((i+max)) % 2 == 1 && lst.get((i+max) - 1)% 2 ==0 ){ //even at odd index..
                    even.remove(even.get(even.size()-1));
                    
                }
            }
        }
        
        return lst.size();
    }
}