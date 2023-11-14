class Calculator:

    def __init__(self, int1, int2):
        self.int1 = int1
        self.int2 = int2
        self.total = 0
        
    def add(self):
        self.total = self.int1 + self.int2
    
    def get_result(self):
        return self.total 
    
    def sub(self):
        self.total = self.int1 - self.int2
        
    def div(self):
        self.total = self.int1 / self.int2
        
    def mul(self):
        self.total = self.int1 * self.int2
    
        
        
        