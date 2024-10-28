
import re

def to_url_title(str):
  # convert to lowercase
  lowercase_str = str.lower()
  # remove non-alphanumeric characters
  url_title = re.sub(r'[^a-zA-Z0-9\s]', '', lowercase_str)
  # replace space with hyphens
  url_title = re.sub(r'\s+', '-', url_title)
  # return url title
  return url_title


