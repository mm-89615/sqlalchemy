import json

from models import Publisher, Book, Shop, Stock, Sale


def read_data(session, file_name):
    with open(f"fixtures/{file_name}") as f:
        data = json.load(f)
    for item in data:
        name = item['model']
        fields = item['fields']
        if name == 'publisher':
            model = Publisher(name=fields['name'])
        if name == 'book':
            model = Book(title=fields['title'],
                         id_publisher=fields['id_publisher'])
        if name == 'shop':
            model = Shop(name=fields['name'])
        if name == 'stock':
            model = Stock(id_shop=fields['id_shop'],
                          id_book=fields['id_book'],
                          count=fields['count'])
        if name == 'sale':
            model = Sale(price=fields['price'],
                         date_sale=fields['date_sale'],
                         count=fields['count'],
                         id_stock=fields['id_stock'])
        session.add(model)
        session.commit()


def get_data(session, publisher):
    data = session.query(Publisher, Book, Stock, Shop, Sale)
    data = data.join(Book, Book.id_publisher == Publisher.id).filter(
        select_publisher_by(publisher) == publisher)
    data = data.join(Stock, Stock.id_book == Book.id)
    data = data.join(Shop, Shop.id == Stock.id_shop)
    data = data.join(Sale, Sale.id_stock == Stock.id)
    if data.first() is None:
        print('Записей не найдено')
    else:
        for publisher, book, stock, shop, sale in data.all():
            print(book.title, shop.name, sale.price, sale.date_sale, sep=' | ')


def select_publisher_by(publisher):
    if publisher.isdigit():
        return Publisher.id
    else:
        return Publisher.name
