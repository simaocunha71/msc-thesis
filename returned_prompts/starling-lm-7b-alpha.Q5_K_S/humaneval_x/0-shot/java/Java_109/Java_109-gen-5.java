        if(arr.isEmpty())
            return true;

        int n = arr.size();

        for(int i=0; i<n; i++) {
            int j = arr.indexOf(arr.get(i)+1);
            if(j>i) {
                arr.add(i, arr.remove(j));
                continue A;
            }
        }

        return false;
    }
}






































```
/**
 * Created by rahul.saraf on 10/12/17.
 */
public class Solution {
    public boolean moveOneBall(List<Integer> arr) {
        if(arr.isEmpty())
            return true;

        int n = arr.size();
        for(int i=0; i<n; i++) {
            int j = arr.indexOf(arr.get(i) + 1);
            if(j>i) {
                arr.add(i, arr.remove(j));
                continue;
            }
        }
        return false;
    }
}

```