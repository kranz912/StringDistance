class Distance(object):
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        self.HammingDistance = self.hammingdistance()
    @classmethod
    def hammingdistance(self):
        distance = 0
        if len(self.str1) != len(self.str2):
            distance = -1
        else:
            for g1, g2  in zip(self.str1, self.str2):
                distance +=  g1!=g2
        return distance