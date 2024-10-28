from operator import itemgetter
def subject_marks(marks):
  return sorted(marks, key=itemgetter(1))  # sort by the second value of each tuple