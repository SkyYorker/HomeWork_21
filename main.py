from classes import Store, Shop, Request




def main():
    storage = {'печеньки': 3, 'dogs': 1, 'boxes': 5}
    shop = {'cookies': 5, 'dogs': 5, 'boxes': 5}


    while True:
        print("Введите команду:")
        user_input = input().split()
        print()
        
        if user_input[0] == 'Курьер' and user_input[1] == 'забирает':
            item = user_input[3]
            count = int(user_input[2])
            if item in storage and storage[item] >= count:
                storage[item] -= count
                print("Нужное количество есть на складе")
                print("Курьер забрал", count, item, "со склад")
                print("Курьер везет", count, item, "со склад в магазин")
                if item in shop:
                    shop[item] += count
                else:
                    shop[item] = count
                print("Курьер доставил", count, item, "в магазин")
                print()
                print("В склад хранится:")
                for item, count in storage.items():
                    print(count, item)
                print()
                print("В магазин хранится:")
                for item, count in shop.items():
                    print(count, item)
            else:
                print("На складе недостаточно", item, "для выполнения заказа")

        elif user_input[0] == 'Доставить' and user_input[3] == 'склад':
            item = user_input[2]
            count = int(user_input[1])
            if item in storage and storage[item] >= count:
                storage[item] -= count
                print("Нужное количество есть на складе")
                print("Курьер забрал", count, item, "со склад")
                print("Курьер везет", count, item, "со склад в магазин")
                if item in shop:
                    shop[item] += count
                else:
                    shop[item] = count
                print("Курьер доставил", count, item, "в магазин")
            else:
                print("Не хватает на складе, попробуйте заказать меньше")

        elif user_input[0] == 'Доставить' and user_input[3] == 'магазин':
            item = user_input[2]
            count = int(user_input[1])
            if item in shop and shop[item] >= count:
                shop[item] -= count
                print("Нужное количество есть в магазине")
                print("Курьер забрал", count, item, "из магазина")
                print("Курьер везет", count, item, "из магазина на склад")
                if item in storage:
                    storage[item] += count
                else:
                    storage[item] = count
                print("Курьер доставил", count, item, "на склад")
            else:
                print("В магазине недостаточно", item, "для выполнения заказа")

        else:
            print("Неизвестная команда")


main()