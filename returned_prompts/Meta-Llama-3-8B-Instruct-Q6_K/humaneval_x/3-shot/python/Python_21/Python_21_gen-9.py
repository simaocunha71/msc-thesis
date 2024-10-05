    min_val = min(numbers)
    max_val = max(numbers)
    return [(x - min_val) / (max_val - min_val) for x in numbers]
# or
    return [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers] # Python 3.9+
# or
    result = []
    for x in numbers:
        result.append((x - min(numbers)) / (max(numbers) - min(numbers)))
    return result # Python 3.7-3.8
# or
    return list(map(lambda x: (x - min(numbers)) / (max(numbers) - min(numbers)), numbers)) # Python 3.7-3.8
# or
    import numpy as np
    return np.array(numbers).clip(min_val, max_val).astype(float) / (max_val - min_val) # Python 3.7-3.8
# or
    import pandas as pd
    df = pd.DataFrame([numbers])
    result = (df.iloc[:, 0] - df.iloc[:, 0].min()) / (df.iloc[:, 0].max() - df.iloc[:, 0].min())
    return result.values.tolist() # Python 3.7-3.8
# or
    import scipy
    result = scipy.stats.norm.ppf(scipy.stats.norm.cdf(numbers, loc=min(numbers), scale=max(numbers)-min(numbers)))
    return result # Python 3.7-3.8
# or
    import statistics
    result = [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]
    return result # Python 3.7-3.8
# or
    import math
    result = [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]
    return result # Python 3.7-3.8
# or
    import statistics
    result = [(x - min(numbers)) / (max(numbers) - min(numbers)) for x in numbers]
    return result # Python 3.7-3.8
# or
    import numpy as np
    result = np.array(numbers).clip(min_val, max_val).astype(float) / (max_val - min_val) # Python 3.7-3.8
# or
    import pandas as pd
    df = pd.DataFrame([numbers])
    result = (