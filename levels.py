
import time


class Level(object):
    images = []

    def __init__(self):
        self.misses = len(self.images)-1

    def gallows(self, misses):
        """Return the gallows image for the given number of misses
        """
        return self.images[misses]

    def animate(self, delay=1):
        """Display each image in turn, with the given delay between frames
        """
        for i in self.images:
            print(i)
            time.sleep(delay)


def getLevels():
    return [l for l in list(globals().values())
            if type(l) == type(Level) 
            and issubclass(l, Level)
            and l != Level]


class LevelHard(Level):
    """ A Level class with 6 misses allowed
    """
    description= "Hard"
    images = ['''\
+--+
|
|
|
+-----+

''','''\
+--+
|
|  |
|
+-----+

''','''\
+--+
|
|  |
| /
+-----+

''', '''\
+--+
|
|  |
| / \ 
+-----+

''', '''\
+--+
| 
| /|
| / \ 
+-----+

''', '''\
+--+
|
| /|\ 
| / \ 
+-----+

''', '''\
+--+
|  |
|  0
| /|\ 
+-/ \-+
 
''']



class LevelEasy(Level):
    description = "Easy"
    images = ['''
XXXXXXXXXXXXXXXXXXXX
XX 
XX
XX 
XX 
XX
XX     
XX      
XX      
XX      
XX     
XX          
XX          
XX       
XX          
XX            
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @     @
XX     \   /
XX      \ /
XX     
XX      
XX      
XX      
XX     
XX          
XX          
XX       
XX          
XX            
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @     @
XX     \   /
XX      \ /
XX    ======= 
XX     =====  
XX     =====  
XX     =====  
XX     +++++ 
XX          
XX          
XX       
XX          
XX            
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @ . . @
XX     \   /
XX      \ /
XX    ======= 
XX     =====  
XX     =====  
XX     =====  
XX     +++++ 
XX          
XX          
XX       
XX          
XX            
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @ . . @
XX     \   /
XX      \-/
XX    ======= 
XX     =====  
XX     =====  
XX     =====  
XX     +++++ 
XX          
XX          
XX       
XX          
XX            
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @ . . @
XX     \ ^ /
XX      \-/
XX    ======= 
XX     =====  
XX     =====  
XX     =====  
XX     +++++ 
XX          
XX          
XX       
XX          
XX            
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @ . . @
XX     \ ^ /
XX      \-/
XX    ======= 
XX     =====  
XX     =====  
XX     =====  
XX     +++++ 
XX        ++
XX        ++
XX        ++
XX        ++
XX            
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @ . . @
XX     \ ^ /
XX      \-/
XX    ======= 
XX     =====  
XX     =====  
XX     =====  
XX     +++++ 
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX            
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @ . . @
XX     \ ^ /
XX      \-/
XX    ======= 
XX     =====  
XX     =====  
XX     =====  
XX     +++++ 
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX        <00>
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @ . . @
XX     \ ^ /
XX      \-/
XX    ========
XX     ===== =
XX     ===== =
XX     ===== =
XX     +++++ 
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX        <00>
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @ . . @
XX     \ ^ /
XX      \-/
XX    ========
XX     ===== =
XX     ===== =
XX     ===== =
XX     +++++ %
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX        <00>
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @ . . @
XX     \ ^ /
XX      \-/
XX   =========
XX   = ===== =
XX   = ===== =
XX   = ===== =
XX     +++++ %
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX        <00>
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @ . . @
XX     \ ^ /
XX      \-/
XX   =========
XX   = ===== =
XX   = ===== =
XX   = ===== =
XX   % +++++ %
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX        <00>
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX
XX     @@@@@
XX    @ . . @
XX     \ ^ /
XX      \-/
XX   =========
XX   = ===== =
XX   = ===== =
XX   = ===== =
XX   % +++++ %
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX     ++ ++
XX   <00> <00>
XXXXXXXXXXXXXXXXXXXX
XX
XX
XX
XX
XX
`'`'`'`'`'`'`'`'`'`'
''','''
XXXXXXXXXXXXXXXXXXXX
XX     |
XX     |
XX     |
XX     |
XX     |
XX     |
XX     @@@@@
XX    @ v v @
XX     \ ^ / 
XX   ===\^/===
XX   = ===== =
XX   = ===== =
XX   = ===== =
XX   % +++++ %
XX     ++ ++
XXXX   ++ ++   XXXX
XX X   ++ ++
XX X   ++ ++
XX X   00 00
XX X   00 00
XX     
`'`'`'`'`'`'`'`'`'`'
''']

