from abc import ABC, abstractmethod




class Storage(ABC):
   
    def __init__(self, items: dict, capacity) -> None:
        self.__items = items
        self.__capacity = capacity

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass
    @abstractmethod    
    def get_unique_items_count(self):
        pass



class Store(Storage):
    def __init__(self, items: dict, capacity=100) -> None:
        self.items = items
        self.capacity = capacity

    def add(self, name, count):
        if name in self.items.keys():
            if self.get_free_space()>= count:
                self.items[name] += count
            else:               
                return "Магазин заполнен"
        else:                   
            if self.get_free_space()>= count:
                    self.items[name] = count
            else:
                return "Магазин заполнен"
            
        
    def remove(self, name, count):
        if self.items[name] > count:
           self.items[name] -= count
        else:
            return "В магазине пусто"


    def get_free_space(self):
        space = 0
        for value in self.items.values():
            space += value
        return self.capacity - space
    

    def get_items(self):
        return self.items
        
    
    def __str__(self) -> str:
        st = ''
        for key, value in self.items.items():
            st += f"{key}:{value}\n"
        return st


    def get_unique_items_count(self):
        return len(self.items.keys())



class Shop(Store):
    def __init__(self, items: dict, capacity) -> None:
        self.items = items
        self.capacity = capacity

    
    def add(self, name, count):
        if name in self.items.keys():
            if self.get_free_space()>= count:
                self.items[name] += count
            else:               
                return "Магазин заполнен"
        else:                   
            if self.get_free_space()>= count:
                    self.items[name] = count
            else:
                return "Магазин заполнен"
            # else:
            #     print("Слишком много товаров")
            #     return "Слишком много товаров" 

    
    def remove(self, name, count):
        if self.items[name] >= count:
           self.items[name] -= count
        else:
            return "В магазине пусто"


    def get_free_space(self):
        space = 0
        for value in self.items.values():
            space += value
        return self.capacity - space


    def get_items(self):
        return self.items

    
    def __str__(self) -> str:
        st = ''
        for key, value in self.items.items():
            st += f"{key}:{value}\n"
        return st


    def get_unique_items_count(self):
        return len(self.items)
    



    

    

# class Request:

#     def __init__(self,request_str):     
#         req_lits = request_str.split()
#         action = req_lits[0]
#         self.__count = int(req_lits[1])
#         self.__items = req_lits[2]
#         self.__from = req_lits[4]
#         self.__to = req_lits[6]
#         if action == "Доставить":
#             self.__from 
#             self.__to
#         elif action == "Забрать":
#             self.__from = req_lits[4]
#             self.__to = None
#         elif action == "Привезти":
#             self.__from = req_lits[4]


#     def move(self):
#         if self.__to:
#             Store.add(self.__items, self.__count)
#         if self.__from:
#             eval(self.__from.remove(self.__item, self.__count))




example_1 = Shop(items={"Telephone": 6, "PC": 5, "TV": 5}, capacity=100)
shop_1 = Store(items={"Telephone": 6, "PC": 5, "TV": 5})


example_1.add('GPU', 100)
example_1.remove('Telephone', 1)
print(example_1.get_free_space())
print(example_1.get_items())
print(example_1.get_unique_items_count())
print(example_1)
# text = "Доставить 12 телевизоров из example_1 в shop_1"
# req = Request(text)
# req.move()
# print(example_1)
# print(shop_1)