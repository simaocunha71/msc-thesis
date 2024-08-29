def filter_values_gt_20(dict):
    return {key: value for key, value in dict.items() if value > 20}

assert filter_values_gt_20