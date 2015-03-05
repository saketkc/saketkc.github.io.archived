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

    def printt(self):
        print str(self.root)

x=SuffixTrie('ABABBC')
graph = networkx.from_dict_of_dicts(x.root)
print networkx.draw_graphviz(graph)
#x.printt()
