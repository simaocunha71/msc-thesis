import java.util.*;
import java.lang.*;

class Solution {
    public boolean moveOneBall(List<Integer> arr) {
        if (arr.size() == 0)
            return true;

        for (int i = 0; i < arr.size() - 1; i++) {
            if (arr.get(i) > arr