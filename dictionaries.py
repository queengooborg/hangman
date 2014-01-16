import os.path
import random

class Dictionary(object):
    words = []

    def __init__(self, name, words):
        self.name = name
        self.words = words

    @classmethod
    def fromFile(cls, sourcefile, name=None):
        """Load a words from a given file.
        Words must be listed one per line, letters only.
        """
        if not name:
            # use the source file name as the default dictionary name
            name, _ = os.path.splitext(os.path.basename(sourcefile))

        words = [w.strip() for w in open(sourcefile).readlines()]

        return cls(name, words)
            
    def randomWord(self):
        i = random.randint(0, len(self.words)-1)
        return self.words[i]

Common = Dictionary.fromFile('common.dict', name="common words")
Animals = Dictionary.fromFile('animals.dict', name="animal names")


def getDicts():
    return [d for d in list(globals().values()) 
                if isinstance(d, Dictionary)]
