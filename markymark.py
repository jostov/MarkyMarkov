import random
#markymark.py
#this gonna make beepi talk
##weirdscience
#maybe each word should look like this
#word, [(neighbor, occurrences)] 
#with three reserved words, _START_, _END_, _TOTAL_
#ehfuckiti'lluseclasses

class MarkyMarkov:
  def __init__(self):
    self.words = {}
    self.words["_START_"] = self.WordData("_START_", None)
  def parse_sentence(self, sentence):
    #The cleansed sentences shall be known as squeakyclean, because they
    #are squeaky and clean.
    squeakyclean = self.clean_sentence(sentence)
    #The used words shall be known as orphans, because life is tragedy.
    #They too shall be discarded into the abyss
    orphan = "_START_"
    for youngbrucewayne in squeakyclean.split(' '):
      if orphan in self.words:
        self.words[orphan].add_word(youngbrucewayne)
      else:
        self.words[orphan] = self.WordData(orphan, youngbrucewayne)
      #The cycle begins anew
      if youngbrucewayne == "_STOP_":
        break
      orphan = youngbrucewayne
  def generate_sentence(self, length=20):
    previous_word = "_START_"
    gibberish = ""
    for i in range(length):
      current_word = self.words[previous_word].next_word()
      if current_word == "_STOP_":
        break
      gibberish += current_word + " "
      previous_word = current_word
    return gibberish
    
  def clean_sentence(self, sentence):
    #Shhh don't tell anyone.
    work = sentence.replace("_STOP_", "")
    work = work.replace("_START_", "")
    return work + " _STOP_"
    
  #It's practically english ya dingus.
  class WordData:
    def __init__(self, key, word=None):
      self.key = key
      self.total = 0
      self.neighbors = []
      if word != None:
        self.add_word(word)
    def add_word(self, word):
      for each in self.neighbors:
        if each.compare(word):
          self.total +=1
          break
      else:
        new_word = self.NeighborData(word)
        self.neighbors.append(new_word)
        self.total += 1
        sentence = ""
        for each in self.neighbors:
          sentence += each.get_word() + " "
    def next_word(self):
      choice = random.randint(0,self.total)
      tracker = 0
      for each in self.neighbors:
        tracker += each.get_occurrences()
        if choice <= tracker:
           retval = each.get_word()
           return retval
      else:
        raise ReferenceError("Bad Code: no neighbor found for" + self.key + "You probably tried to generate a sentence without adding data, didn't you? Not so good.")



    class NeighborData:
      def __init__(self, word):
        self.occurrences = 1
        self.word = word
      def compare(self, word):
        if word == self.word:
          self.occurrences += 1
          return True
        return False
      def get_occurrences(self):
        return self.occurrences
      def get_word(self):
        return self.word
def 

if __name__ == '__main__':
  sentence1 = "butts are huge and butts are big"
  sentence2 = "i don't think the only thing to talk about is butts"
  sentence3 = "what is the point of all these butts"
  sentence4 = "who would waste time on this dumb thing"
  thing = MarkyMarkov()
  thing.parse_sentence(sentence1)
  thing.parse_sentence(sentence2)
  thing.parse_sentence(sentence3)
  thing.parse_sentence(sentence4)
  print thing.generate_sentence()
