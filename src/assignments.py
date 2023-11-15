# define your methods here.
# ex1() - ex10()
from pprint import pprint 
from src.WordCounter import WordCounter
from src.TaxMan import TaxMan
from src.Calculator import Calculator
from src.CarCollector import CarCollector
from src.Dwarf import Dwarf
from src.Fighter import Fighter
from src.Invoice import Invoice
import inspect 


def ex1():
    print("hello")

def ex2():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    def filter_males(update_list):
        male_list = list(filter(lambda p:p['sex'] == 'male', update_list))
        return male_list
    
    new_list = filter_males(people_list)
    print(new_list)


def ex3():
    people_list = [
    {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
]
    
    def calc_bmi(people_list):
        bmiCalc = round (people_list['weight_kg']/people_list['height_meters'] ** 2,1)
        people_list.update({'bmi':bmiCalc})
        return people_list
        
    bmilist = list(map(calc_bmi,people_list))
    print(bmilist) 


def ex4():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    def get_people(input_list):
        # new_list = list([x for x in input_list if x['age'] >= 15])
        # name_list = [] 
        # for elem in new_list:
        #     name_list.append(elem['name'])
        new_list = [p['name'] for p in input_list if p['age'] >= 15]
        return new_list
    
    new_list = get_people(people_list)
    print(new_list)

def ex5():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()

    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.

def ex6():
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())

def ex7():
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())

def ex8():
    pprint(CarCollector.get_data()) 

def ex9():
    f = Fighter(18)
    d = Dwarf(15)
    print(f)
    print(d)
    f.fight(d)
    d.fight(f)
    print(f)
    print(d)

def ex10():
    data = [
        "1, 2322, 10.00, False",
        "2, 5435, 60.30, True",
        "3, 3433, 15.63, False",
        "4, 8439, 12.77, False",
        "5, 3424, 11.34, False",
    ]
    
    invoices = [Invoice(*item.split(', ')) for item in data]
    pprint(invoices) 