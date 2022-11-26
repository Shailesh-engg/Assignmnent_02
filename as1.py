def last(n):
     return n[-1]

def sort_list_last(tup):
  return sorted(tup, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
