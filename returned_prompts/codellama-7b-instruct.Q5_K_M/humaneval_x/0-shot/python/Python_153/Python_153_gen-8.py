
class_name = class_name.title()
extensions = sorted(extensions, key=lambda x: (x.count(x.upper()), x.count(x.lower())))
return class_name + '.' + extensions[-1]

