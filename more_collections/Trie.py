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
        self.depth = max(self.depth, len(word))
        self.size += 1
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.is_word = True

    def delete(self, word):
        nodes = [self.root]
        node = self.root
        for letter in word:
            if letter not in node.children:
                return
            nodes.append(node.children[letter])
            node = node.children[letter]
        self.size -= 1
        for i in range(len(nodes) - 1, 0, -1):
            if nodes[i].is_word or nodes[i].children:
                return
            else:
                del nodes[i - 1].children[word[i-1]]


