    public Optional<Integer> prodSigns(List<Integer> arr) {
        if(arr.isEmpty()) {
            return Optional.empty();
        }
        int signProduct = 1;
        int sum = 0;
        for(int num : arr) {
            if(num == 0) {
                return Optional.empty();
            }
            signProduct *= Math.signum(num);
            sum += Math.abs(num);
        }
        return Optional.of(sum * signProduct);
    }
    // Math.signum returns 1 for positive numbers, -1 for negative numbers and 0 for 0. This is used to calculate the product of signs.
    // If the array contains 0, the product of signs will be 0 and the sum will also be 0, so we return Optional.empty() to indicate that the array is invalid for this operation.
    // Otherwise, we return the product of the sum of magnitudes of integers and the product of all signs, represented by the Optional.of method.  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  }  } 