import string

alphabet = list(string.ascii_uppercase)

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [[] for item in range(array_size)]

  def hash(self, key):
    hash_value = alphabet.index(key)
    return hash_value

  def assign(self, key, value):
    array_index = self.hash(key)
    current_array_value = self.array[array_index]

    if value in current_array_value:
      return

    self.array[array_index].append(value)

  def retrieve(self, key):
      array_index = self.hash(key)
      return self.array[array_index]

def alphabetise(category, dictionary):
    alphabetised = HashMap(26)
    for dict in list(dictionary.values()):
        if isinstance(dict[category], tuple):
            for item in dict[category]:
                alphabetised.assign(item[0], item)
        else:
            alphabetised.assign(dict[category][0], dict[category])
    
    return alphabetised
   
