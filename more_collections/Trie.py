class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.depth = 0
        self.size = 0
    
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    # def delete(self, word):
    #     node = self.root

