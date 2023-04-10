import json
class Data:
    def __init__(self , data):
        with open(data, 'r') as f:
            main_file = f.read()
            self.data = json.loads(main_file)
    #вывод товаров с ценой меньше средней
    def get_avg_data(self):
        #находим среднюю цену
        prices = [item['price'] for item in self.data]
        avg_price = sum(prices) / len(prices)
        avg_data = []
        #создаем список товаров с ценой, меньше средней 
        for item in self.data:
            if item['price'] <= avg_price:
                avg_data.append(item)
        return json.dumps(avg_data,  ensure_ascii=False)