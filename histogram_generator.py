def histogram_generator(string):
  histogram = {}
  for char in string:
    if char in histogram:
      histogram[char] += 1
    else:
      histogram[char] = 1
  return histogram

