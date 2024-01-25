import AIChat
import random

from datetime import datetime

#食物資料庫
Food_Database = [
    "滷肉飯", "牛肉麵", "三杯雞", "炸雞", "烤魚", "義大利麵", "壽司", "披薩", "火鍋", "炒麵",
    "炸蝦", "燒烤", "湯鍋", "咖哩飯", "拉麵", "鍋貼", "生煎包", "蒸魚", "豆腐脆皮", "沙拉",
    "烏龍麵", "魚麵", "麻辣燙", "韓式炸雞", "雞排", "薯條", "牛排", "墨西哥捲餅", "東坡肉", "花生醬三明治",
    "爌肉飯", "擔仔麵", "餛飩麵", "乾麵", "肉包", "燒賣", "蚵仔煎", "臭豆腐", "鹽酥雞", "花生酥", "泡麵", "西北風",
    "臭臭鍋", "石頭火鍋", "米粉湯", "涼麵", "豬血湯", "花生湯", "麻辣烫", "担担面", "炸鱼蛋", "烤地瓜", "車輪餅",
    "蔥抓餅", "爆漿蛋糕", "布丁", "冰淇淋", "泡芙", "可頌", "提拉米蘇", "抹茶蛋糕", "蛋糕捲", "雞肉飯", "涼麵"
]

#機器人生日
BirthDay = {
    "year": 2023,
    "month": 10,
    "day": 24
}

#遊戲資料庫
Game_Database = [
    "原神","genshin","傳說對決","minecraft","世界計畫","pjsk","崩壞星芎:鐵道","崩壞星穹鐵道","崩鐵",
    "崩壞","啤酒燒烤","roblox","機器磚塊","開心水族箱","王者榮耀","歐洲卡車模擬器2","歐洲卡車模擬器",
    "卡車模擬器2","卡車模擬器","普羅世界","普羅","d4dj","maimai DX","maimaiDX","maimai","Apex",
    "中二節奏","chunithm","raft","switch","動物森友會","動森"
]

#未知的回應
unknow_reply = [
    "我不知道我要說什麼...",
    "我很認真思考這句話，但我不知道我要講啥欸",
    "蛤?Whats?你說啥?",
    "?我看不懂",
    "呃...我的記憶沒有這種東西出現過",
    "這是什麼?",
    "窩不知道，你在說什麼?",
    "你怎麼會覺得我知道這東西呢...?",
    "我...我想不到有什麼回應了QWQ"
]

#過濾
Filter_Word = [
    
]

#替換字，Onlyone是限定只有相等的單字時觸發
#例如 : 棗安你好 > 早安你好
#但是 : 棗，你好 > 棗，你好
Replace_Word = [
    {
        "Key": "甚麼",
        "Replace": "什麼",
        "Onlyone" : False
    },
    {
        "Key": "棗安",
        "Replace": "早安",
        "Onlyone" : False
    },
    {
        "Key": "棗阿",
        "Replace": "早阿",
        "Onlyone" : False
    },
    {
        "Key": "棗",
        "Replace": "早",
        "Onlyone" : True
    }
]

def calculate_age():
    #生日處理，判斷年齡
    Today_Day = {
        "year": int(datetime.now().strftime("%Y")),
        "month": int(datetime.now().strftime("%m")),
        "day": int(datetime.now().strftime("%d"))
    }
    
    BirthDay_Total_Day = BirthDay["month"] * 30 + BirthDay["day"]
    Today_Day_Total_Day = Today_Day["month"] * 30 + Today_Day["day"]
    
    Age = Today_Day["year"] - BirthDay["year"]

    if(BirthDay_Total_Day < Today_Day_Total_Day):
        Age = Age + 1
    
    return Age


def Chat_Program(input_message,BotName, Creator):
    #過濾
    for i in Filter_Word:
        if(input_message.find(i) != -1):
            return "Filtered"
    
    #替換近似詞
    for i in Replace_Word:
        if i["Onlyone"] == True and input_message == i["Key"] :
            input_message = i["Replace"]
        elif i["Onlyone"] == False and input_message.find(i["Key"]) != -1:
            input_message = input_message.replace(i["Key"], i["Replace"])  

    #食物轉參數
    for i in Food_Database:
        input_message = input_message.replace(i, "{__FOOD_DATABASE}")          

    #空白的輸入，純屬呼叫機器人
    if(input_message == ""):
        input_message = "{__CELL_BOT}"

    #轉小寫，方便之後處裡    
    input_message = input_message.lower()

    #將機器人名稱替換成參數
    input_message = input_message.replace(BotName, "{__BOT_NAME}")

    #將遊戲替換成參數
    for i in Game_Database:
        input_message = input_message.replace(i, "{__GAME}")

    #AI處理，回應
    AI_Response = AIChat.chat(input_message)

    #替換各種參數
    AI_Response = AI_Response.replace("{__BOT_NAME}", BotName)
    AI_Response = AI_Response.replace("{__NOW_TIME}", str(datetime.now().strftime("%H點%M分")))
    AI_Response = AI_Response.replace("{__FOOD_DATABASE}", random.choice(Food_Database))
    AI_Response = AI_Response.replace("{__CREATOR_NAME}", Creator)
    AI_Response = AI_Response.replace("{__DICE}", str(random.randint(1, 6)))
    AI_Response = AI_Response.replace("{__AGE}",str(calculate_age()))
    AI_Response = AI_Response.replace("{__BIRTHDAY}", str(BirthDay["year"]) + "年" + str(BirthDay["month"]) + "月" + str(BirthDay["day"]) + "日")
    AI_Response = AI_Response.replace("{__UNKNOW_REPLY}", random.choice(unknow_reply))

    #輸出
    return AI_Response