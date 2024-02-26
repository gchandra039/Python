
def get_positions(pattern, word_length):
  len_pattern = len(pattern)
  repitations = word_length // len_pattern
  extra = word_length % len_pattern
  positions = pattern * repitations + pattern[:extra]
  return positions

def get_new_word(word, positions, N):
  new_word = ""
  for i in range(1, N+1):
    for j in range(len(positions)):
      if positions[j] == i:
        new_word += word[j]
  return new_word

# get_positions(pattern, 14)
def main():
  S = input("enter string: ")
  N = int(input())
  pattern = list(range(1,N+1)) + list(range(N-1,1,-1))
  word_length = len(S)
  positions = get_positions(pattern, word_length)
  a = (len(positions))
  new_word = get_new_word(S, positions, N)
  print(new_word)
  print(a)


main()
