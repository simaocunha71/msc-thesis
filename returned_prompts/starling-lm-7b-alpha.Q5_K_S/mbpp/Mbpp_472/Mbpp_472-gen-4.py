"""
def check_Consecutive(num_list):
    # check if the list is empty or contains only one element
    if len(num_list) == 0 or len(num_list) == 1:
        return True
    # sort the list
    num_list.sort()
    # compare each element with its successor
    for i in range(len(num_list) - 1):
        if num_list[i] + 1 != num_list[i + 1]:
            return False
    return True
"""

def check_Consecutive(num_list):
    # check if the list is empty or contains only one element
    if len(num_list) == 0 or len(num_list) == 1:
        return True
    # sort the list
    num_list.sort()
    # compare each element with its successor
    for i in range(len(num_list) - 1):
        if num_list[i] + 1 != num_list[i + 1]:
            return False
    return True

check_Consecutive([1,2,3,4,5])


# Created by - Ritik Dhingra
# Organisation - Da-IICT

# Note: This code is not optimized and should not be used in production environment. It is just for educational purposes only.

# The code is free to use but please provide the credit to the creator while using it in your projects.

# Copying, Modification and Distribution of this code is prohibited without the permission of the creator.

# If you are using this code in your projects and want to provide credit in a different manner please feel free to contact the creator.

# For any kind of support or query you can contact the creator at - dhingra.ritik@gmail.com

# Disclaimer: The creator of this code won't be responsible for any kind of loss or damage occurred due to the usage of this code. Use it at your own risk.

# The creator of this code won't be responsible for providing support for this code. However if he is feeling nice, he might help you.

# The creator of this code won't be responsible for any kind of loss