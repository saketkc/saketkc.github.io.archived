import networkx
import matplotlib.pyplot as plt
class SuffixTrie(object):
    def __init__(self, T):
        T+='$'
        self.root = {}
        for i in range(0, len(T)+1):
            string = T[i:]
            root = self.root
            for character in string:
                if character in root.keys():
                    pass
                else:
                    root[character] = {}
                root = root[character]

    def printTrie(self):
        print str(self.root)

    def searchString(self, s):
        root = self.root
        for character in s:
            if character not in root.keys():
                return False
            root = root[character]
        return root

    def perform_edge_compression(self):
        pass

    def get_offset(self,T,substring):
        pass

x = SuffixTrie('ABABBC')
graph = networkx.from_dict_of_dicts(x.root)
print x.searchString('BB')
