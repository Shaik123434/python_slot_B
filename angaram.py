
def  anagram_check(keywords):
  anagrams = defaultdict(list)
  for i in keywords:
   histogram = tuple(Counter(i).items())
   anagrams[histogram].append(i)
  return list(anagrams.values())
keywords = ("a")
print(anagram_check(keywords))
