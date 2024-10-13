class Store:
    """Класс, представляющий магазин с его названием, адресом и ассортиментом товаров."""

    def __init__(self, name, address):
        """Конструктор, который инициализирует название, адрес и пустой ассортимент товаров."""
        self.name = name
        self.address = address
        self.items = {}  # Словарь товаров, где ключ — название товара, значение — цена

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в магазин {self.name} по цене {price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' был удалён из магазина {self.name}.")
        else:
            print(f"Товар '{item_name}' не найден в магазине {self.name}.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товара нет, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден в магазине {self.name}.")

    def display_items(self):
        """Отображает все товары в ассортименте магазина."""
        if not self.items:
            print(f"В магазине {self.name} нет товаров.")
        else:
            print(f"Ассортимент магазина {self.name}:")
            for item, price in self.items.items():
                print(f" - {item}: {price} руб.")


# Пример использования класса Store
if __name__ == "__main__":
    # Создание магазина
    store1 = Store("Магазин у дома", "ул. Ленина, 12")

    # Добавление товаров в магазин
    store1.add_item("apples", 50)
    store1.add_item("bananas", 60)
    store1.add_item("milk", 80)

    # Отображение всех товаров
    store1.display_items()

    # Получение цены товара
    price = store1.get_price("apples")
    if price is not None:
        print(f"Цена на яблоки: {price} руб.")
    else:
        print("Яблоки не найдены в магазине.")

    # Обновление цены товара
    store1.update_price("bananas", 65)

    # Удаление товара
    store1.remove_item("milk")

    # Отображение всех товаров после удаления и обновления
    store1.display_items()
