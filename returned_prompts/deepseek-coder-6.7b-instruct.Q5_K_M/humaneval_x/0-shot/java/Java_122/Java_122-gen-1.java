        int sum = 0;
        for(int i = 0; i < k; i++){
            if(arr.get(i) >= 0 && arr.get(i) <= 99){
                sum += arr.get(i);
            }
        }
        return sum;
    }
}

*/

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<Integer> arr = Arrays.asList(111,21,3,4000,5,6,7,8,9);
        int k = 4;
        System.out.println(s.addElements(arr, k)); // Output: 24
    }
}

```

## 문제 해결 설명

주어진 정수 배열의 첫 번째 k 요소에 대해서만 반복문을 수행하며, 각 요소가 1과 99 사이의 값을 가지는지 확인합니다. 만약 그렇다면, 해당 요소를 합에 더합니다. 반복문이 끝나면, 모든 요소를 처리하고 합이 반환됩니다.

문제에서 