from .JsonObject import *
from exceptions.Exceptions import *
from util.Stringify import *

class JSONArray(list) :
    
    def __init__(self) :
        self.data = list()
    
    def size(self) :
        return len(self.data)

    def get(self, i) :
        return self.data[i]

    def append(self, i) :
        self.data.append(i)

    def __getitem__(self, i) :
        return self.data[i]

    def __setitem__(self, i, value) :
        self.data[i] = value

    def getJSONObject(self, i) :
        ret = self.data[i]
        if isinstance(ret, JsonObject) :
            return ret
        raise JsonTypeErrorException('JSONObject', str(type(ret)))

    def getJSONArray(self, i) :
        ret = self.data[i]
        if isinstance(ret, JSONArray) :
            return ret
        raise JsonTypeErrorException('JSONArray', str(type(ret)))
    
    def __str__(self) :
        return arrayToString(self, 0)

    def __iter__(self) :
        return iter(self.data)
    
    def __eq__(self, array) :
        if isinstance(array, JSONArray) :
            if not self.size() == array.size() :
                return False
            for i in range(0, self.size()) :
                if not self.get[i] == array.get(i) :
                    return False
            return True
        return False