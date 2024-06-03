import pymongo as py

clint = py.MongoClient("mongodb://localhost:27017")
db = clint["test"]

class Status:
    def save_status(collection, status, time):
        collection = db[collection]
        try:
            data = collection.find_one_and_delete({})
        except:
            pass
        new_stat = {"Status":status, "Time":time}
        data = collection.insert_one(new_stat)
        return data

    def find_status(collection):
        collection = db[collection]
        data = collection.find_one({})
        return data["Status"]

class Orders:
    def close_buy_sell(collection, symbol, profit, magic, lot, stg, price, zscor, volume, time, orderType, indecator, timeFrame):
        collection = db[collection]
        new_data = {"Symbol":symbol, "Profit":profit, "Magic":magic, "Lot":lot, "Stg":stg, "Price":price, "Zscor":zscor, "Volume":volume, "Time":time ,"OrderType":orderType, "Indecator":indecator, "TimeFrame":timeFrame}
        return collection.insert_one(new_data)
    
    def opene_buy_sell(collection, symbol, magic, lot, stg, price, zscor, volume, time, orderType, indecator, timeFrame):
        collection = db[collection]
        new_data = {"Symbol":symbol, "Magic":magic, "Lot":lot, "Stg":stg, "Price":price, "Zscor":zscor, "Volume":volume, "Time":time ,"OrderType":orderType, "Indecator":indecator, "TimeFrame":timeFrame}
        return collection.insert_one(new_data)
    



