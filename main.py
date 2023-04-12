from classes import Store, Shop, Request


storage = Store(items={'печеньки': 5, 'собачки': 1, 'коробки': 5})
shop = Shop(items={'печеньки': 5, 'собачки': 5, 'коробки': 5})

warehouses = [storage, shop]

print("Для выхода введите Q")

while True:
    print("Введите команду:")
    user_input = input().split()
    reqest = Request(warehouses, user_input)

    print()

    if user_input[0] == 'Курьер' and user_input[1] == 'забирает' and reqest.from_place == 'склад':
        item = reqest.product
        count = reqest.amount
        if item in storage.get_items() and storage.get_items()[item] >= count:
            storage.remove(item, count)
            print("Нужное количество есть на складе")
            print(f"Курьер забрал {count} {item} со склад\nКурьер везет {count} {item} со склад в магазин")                      
            if shop.add(item, count):
                shop.add(item, count)
                print(f"Курьер доставил {count} {item} в магазин\n")
            else:
                print(f"В магазине недостаточно места")
            print(f"В склад хранится:\n{storage}\nВ магазин хранится:\n{shop}")
        elif item in storage.get_items() and storage.get_items()[item] < count and shop.get_items()[item] > count:
            print("Не хватает на складе, попробуйте заказать меньше")

    elif user_input[0] == 'Доставить' and reqest.to_place == 'склад':
        item = reqest.product
        count = reqest.amount
        if item in storage.get_items() and storage.get_items()[item] >= count:
            shop.remove(item, count)
            print("Нужное количество есть на складе")
            print(f"Курьер забрал {count} {item} со склада\nКурьер везет {count} {item} из магазин в склад")
            if storage.add(item, count):
                storage.add(item, count)
                print(f"Курьер доставил {count} {item} в магазин\n")
            else:
                print(f"В магазине недостаточно места")            
            print(f"Курьер доставил {count} {item} на склад")
            print(f"В склад хранится:\n{storage}\nВ магазин хранится:\n{shop}")
        elif item in storage.get_items() and storage.get_items()[item] < count and shop.get_items()[item] > count:
            print("Не хватает на складе, попробуйте заказать меньше")
        else: 
            print(f"В магазине недостаточно {item} для выполнения заказа")

    elif user_input[0] == 'Доставить' and reqest.to_place == 'магазин':
        item = reqest.product
        count = reqest.amount
        if item in shop.get_items() and storage.get_items()[item] >= count:
            storage.remove(item, count)
            print("Нужное количество есть на складе")
            print(f"Курьер забрал {count} {item} из склада\nКурьер везет {count} {item} со склад в магазин")           
            if shop.add(item, count):
                shop.add(item, count)
                print(f"Курьер доставил {count} {item} в магазин\n")
            else:
                print(f"В магазине недостаточно места")
            print(f"В склад хранится:\n{storage}\nВ магазин хранится:\n{shop}")
        elif item in storage.get_items() and storage.get_items()[item] < count and shop.get_items()[item] > count:
            print("Не хватает на складе, попробуйте заказать меньше")           
    if user_input[0] == 'q' or user_input[0] == 'Q':
        break          
    else:
        print("Неизвестная команда")

    