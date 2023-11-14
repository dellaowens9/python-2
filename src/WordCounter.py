class WordCounter:
    
    
    def __init__(self, sentence):
        self.sentence = sentence

    def count_words(self):
        word_list = len(self.sentence.split(" "))
        return word_list 
        
    def get_word_count(self): 
        word_list = len(self.sentence.split(" "))
        return word_list
    
    def get_shortest_word(self):
        word_list = self.sentence.split(' ')
        min_word = min(word_list, key=len)
        min_word_length = len(min_word)
        return f"Min word: {min_word} and length: {min_word_length}"

    def get_longest_word(self):
        word_list = self.sentence.split(' ')
        max_word = max(word_list, key=len)
        max_word_length = len(max_word)
        return f"Max word: {max_word} and length: {max_word_length}"  