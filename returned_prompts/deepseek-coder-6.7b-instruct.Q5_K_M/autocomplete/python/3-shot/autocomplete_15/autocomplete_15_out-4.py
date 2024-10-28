    if  (rv.status_code  !=  200):
      raise Exception(f"{method} failed with status: {rv.status_code}")
