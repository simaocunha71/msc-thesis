        if (arr.isEmpty()) {
            return true;
        }

        //check if the array is already sorted in non-decreasing order
        if (arr.get(0) <= arr.get(arr.size() - 1)) {
            return true;
        }

        //check if the array is already sorted in non-decreasing order
        if (arr.get(arr.size() - 1) <= arr.get(0)) {
            return false;
        }

        //check if the array is sorted in non-decreasing order after performing one right shift operation
        if (arr.get(arr.size() - 1) >= arr.get(arr.size() - 2)) {
            return true;
        }

        //check if the array is sorted in non-decreasing order after performing one right shift operation
        if (arr.get(arr.size() - 2) >= arr.get(arr.size() - 1)) {
            return false;
        }

        //check if the array is sorted in non-decreasing order after performing one right shift operation
        if (arr.get(arr.size() - 1) >= arr.get(arr.size() - 3)) {
            return true;
        }

        //check if the array is sorted in non-decreasing order after performing one right shift operation
        if (arr.get(arr.size() - 3) >= arr.get(arr.size() - 1)) {
            return false;
        }

        //check if the array is sorted in non-decreasing order after performing one right shift operation
        if (arr.get(arr.size() - 1) >= arr.get(arr.size() - 4)) {
            return true;
        }

        //check if the array is sorted in non-decreasing order after performing one right shift operation
        if (arr.get(arr.size() - 4) >= arr.get(arr.size() - 1)) {
            return false;
        }

        //check if the array is sorted in non-decreasing order after performing one right shift operation
        if (arr.get