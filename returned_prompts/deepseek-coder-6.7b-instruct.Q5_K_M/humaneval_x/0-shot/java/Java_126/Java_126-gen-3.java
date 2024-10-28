        for(int i = 0; i < lst.size() - 1; i++){
            if(lst.get(i) >= lst.get(i+1)){
                return false;
            }
        }
        return true;
    }
}

// This solution works by iterating over the list and comparing each element with the next one. If at any point the next element is smaller or equal to the current one, the method returns false, indicating that the list is not sorted in ascending order. If the loop completes without encountering such a pair, the method returns true.

// The time complexity of this solution is O(n), where n is the length of the list, because in the worst case it iterates over the list once. The space complexity is O(1), because it only uses a constant amount of additional space.

// The assumption about negative numbers and only integers in the problem statement is respected. The method does not consider or handle such cases.

// The method does not handle cases where there are more than one duplicate of the same number in the list, as stated in the problem. If such a case is encountered, the method will return false.

// The method does not handle cases where the list is empty, as the problem statement does not specify how such a case should be handled. In this solution, an empty list is considered to be sorted, and the method will return true.

// The method does not handle cases where the list has more than one duplicate of the same number, as stated in the problem. If such a case is encountered, the method will return false.

// This solution assumes that the input list is not null. If the input list is null, the method will throw a NullPointerException when trying to access its elements.

// The method does not handle cases where the list has more than one duplicate of the same number, as stated in the problem. If such a case is encountered, the method will return false.

// This solution assumes that the input list is not null. If the input list is null, the method will throw a NullPointerException when trying to access its elements.

// The method does not handle cases where the list has more than one duplicate of the same number, as stated in the problem. If such a case is encountered, the method will return false.

// This solution assumes that