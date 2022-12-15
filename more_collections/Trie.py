class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    """
    Note: Decided halfway through to not track depth (size of longest entry) becuase I don't
    know how I would change it upon deletion? Could track all depths using maxheap BUT kind
    of makes this too long for its purpose (copy and paste for leetcode :/)
    """
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def getsize(self):
        return self.size

    def getdepth(self):
        return self.depth
    
    def insert(self, word):
        self.depth = max(self.depth, len(word))
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        if not node.is_word:
            self.size += 1
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_word

    def startswith(self, prefix: str) -> bool:
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True

    def delete(self, word):
        nodes = [self.root]
        node = self.root
        for letter in word:
            if letter not in node.children:
                raise ValueError(f"delete: {word} not in trie")
            nodes.append(node.children[letter])
            node = node.children[letter]
        if not node.is_word:
            raise ValueError(f"delete: {word} not in trie")
        self.size -= 1
        for i in range(len(nodes) - 1, 0, -1):
            if nodes[i].is_word or nodes[i].children:
                return
            else:
                del nodes[i - 1].children[word[i-1]]


