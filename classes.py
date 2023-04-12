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
    def __init__(self, items: dict, capacity=100, name=str) -> None:
        self.__items = items
        self.__capacity = capacity
        self.__name = name

    def add(self, name, quantity):
        if len(self.__items) >= 5 or self.get_free_space() < quantity:
            return False
        if name in self.__items:
            self.__items[name] += quantity
        else:
            self.__items[name] = quantity
        

    def remove(self, name, quantity):
        if name in self.__items:         
            if quantity > self.__items[name]:
                    return False
            else:
                self.__items[name] = max(0, self.__items[name] - quantity)

    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)

    
    def __str__(self) -> str:
        st = ''
        for key, value in self.__items.items():
            st += f"{value} {key}\n"
        return st



class Shop(Store):
    def __init__(self, items: dict, capacity=25, name=str) -> None:
        self.__items = items
        self.__capacity = capacity
        self.__name = name

    
    def add(self, name, quantity):
        if len(self.__items) >= 5 or self.get_free_space() < quantity:
            return False      
        if name in self.__items:
            self.__items[name] += quantity
        else:
            self.__items[name] = quantity
        

    def remove(self, name, quantity):
        if name in self.__items:         
            if quantity > self.__items[name]:
                    return False
            else:
                self.__items[name] = max(0, self.__items[name] - quantity)    
        

    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)

    
    def __str__(self) -> str:
        st = ''
        for key, value in self.__items.items():
            st += f"{value} {key}\n"
        return st


class Request:
    def __init__(self, warehouses, request_string):
        self.warehouses = warehouses
        request_list = request_string
        if len(request_list) == 6:
            self.amount = int(request_list[2])
            self.product = request_list[3]
            self.from_place = request_list[5]
        elif len(request_list) == 7:           
            self.amount = int(request_list[1])
            self.product = request_list[2]
            self.from_place = request_list[4]
            self.to_place = request_list[6]
        else:
            None

# example_1 = Shop(items={"Telephone": 6, "PC": 5, "TV": 50, 'GPU': 1, 'CPU': 1}, capacity=100, name="shop_1")
# shop_1 = Store(items={"Telephone": 6, "PC": 5, "TV": 5}, name="example_1")


# example_1.add('PB', 1)
# example_1.remove('Telephone', 7)
# print(example_1.get_free_space())
# print(example_1.get_items())
# print(example_1.get_unique_items_count())
# print(example_1)
# storages = [example_1, shop_1]
# text = "Курьер забирает 3 печеньки из склад"
# # req = Request(text)
# # req.move()
# # print(example_1)
# # print(shop_1)
# request = Request(storages, text)
# # q = example_1.get_items()
# # print(q.())
# print(request.amount)