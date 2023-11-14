class TaxMan:

    def __init__(self, item_list, perecentage):
        self.item_list = item_list
        self.__percentage = perecentage
        self.__total = 0
    
    def calc_total(self):
        percent_int = float(self.__percentage.strip('%')) / 100 
        item_cost = [x['price'] for x in self.item_list]
        
        for elem in item_cost:
            item_tax = (elem + elem * percent_int) 
            self.__total += item_tax
       
        return self.__total 
    
    def get_total(self):
        return (self.__total) 