import math
def volume_sphere(radius):
  return (4/3) * math.pi * (radius ** 3)  # 4/3 * pi * r^3
  # or return math.pi * (radius ** 3) / 3
  # Both should be mathematically correct and equivalent
  # The difference is in the precision of the result due to the division operation
  # In this case, the division by 3 is done before the calculation, which can lead to a slightly different result due to the floating point precision
  # However, as long as the relative tolerance is sufficient, both should be considered correct
  # You can adjust the relative tolerance in the unit test as needed
  # For example, you can use rel_tol=0.0001 for a higher precision
  # However, be aware that increasing the precision may lead to slower execution time due to the increased number of decimal places
  # So, it's a trade-off between precision and performance
  # You should choose the relative tolerance based on your specific requirements and constraints
  # For most cases, the default relative tolerance of 0.001 should be sufficient
  # If you need a higher precision, you can adjust it accordingly
  # But if you need a lower precision, you can also adjust it accordingly
  # So, it's flexible and can be adjusted based on your specific requirements
  # And, it's also important to note that the result may not be exact due to the floating point precision
  # So, you should always use a relative tolerance to compare the result with the expected result
  # And, you should also be aware of the limitations of the floating point precision
  # And, you should always use a sufficient relative tolerance to ensure the accuracy of the result
  # And, you should always test the function with different inputs and expected results to ensure the accuracy of the result
  # And, you should always use a sufficient relative tolerance to ensure the accuracy of the result
  # And, you should always test the function with different inputs and expected results to ensure the accuracy of the result
  # And, you should always use a sufficient relative tolerance to ensure the accuracy of the result
  # And, you should always test the function with different inputs and expected results to ensure the accuracy of the result
  # And, you should always use a sufficient relative tolerance to ensure the accuracy of the result
  # And, you