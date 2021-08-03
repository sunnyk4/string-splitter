import re

class TagManipulator():    
    '''def parse_string(self, tags):
        result = []

        if len(tags) < 1 :
            return result

        return result'''
    def parse_string(self, tags, regex=""):
        result = []

        tempResult = re.split( regex, tags )
        if( len(tempResult[0]) > 0 ):
            result = tempResult  

        return result