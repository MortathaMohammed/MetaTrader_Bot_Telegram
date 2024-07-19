import pymongo as py

clint = py.MongoClient("mongodb://localhost:27017")
db = clint["change"]

class Status:
    def save_status(collection, status, time):
        collection = db[collection]
        data = collection.find_one_and_delete({})
        new_stat = {"Status":status, "Time":time}
        data = collection.insert_one(new_stat)
        return data

    def find_status(collection):
        collection = db[collection]
        data = collection.find({})
        for dt in data:
            stat = dt["Status"]
        return stat

class Data:
    def save_data_symbol(collection, symbol, close, volume):
        collection = db[collection]
        data = collection.find_one_and_replace({"symbol":symbol}, {"symbol":symbol ,"close":close, "volume":volume})

        # new_stat = {"close":close, "volume":volume}
        # data = collection.insert_one(new_stat)
        return data
    
    def find_data_symbol(collection, symbol):
        collection = db[collection]
        data = collection.find({})
        for dt in data:
            if dt["symbol"] == symbol:
                close = dt["close"]
                volume = dt["volume"]
                
        return  [close, volume]
    
    def save_info(collection, symbol, volume, price):
        collection = db[collection]
        try:
            collection.find_one_and_delete({"Symbol":symbol})
            new_data = {"Symbol":symbol, "Volume":volume, "Price":price}
        except:
            new_data = {"Symbol":symbol, "Volume":volume, "Price":price}
        return collection.insert_one(new_data)

    def find_info_second(collection, symbol, volume, price):
        collection = db[collection]
        try:
            data = collection.find_one({"Symbol":symbol})
            return [data["Symbol"], data["Volume"], data["Price"]]
        except:
            new_data = {"Symbol":symbol, "Volume":volume, "Price":price}
            collection.insert_one(new_data)
            return [symbol, volume, price]
        

# print(Data.find_info_second("second", "XAUUSD", 5, 324))

