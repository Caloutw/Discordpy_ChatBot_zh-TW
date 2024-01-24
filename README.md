# Discordpy_ChatBot_zh-TW
A Chatbot AI Project with Tensorflow

Python新手，程式碼真的是東拼西湊，請見諒

這是基於 Tensorflow 和 Keith Flagg 提供之原始碼開發的AI神經網路回應機器人

因為之前被BrainJS搞了，所以打算找一個可以GPU加速的身經網路學習框架

阿好死不死公司電腦沒有NVDIA卡，沒辦法玩Pytorch，所以只能退而求其次搞個Python

反正這東西內顯也可以加速，嗚呼~

# 安裝、開始使用
必要插件有 Tensorflow、numpy、tflearn、nltk、jieba、DiscordPy

python版本必須是 3.6 ~ 3.9

https://www.python.org/downloads/release/python-390/

安裝Tensorflow
```
pip install tenforflow==2.12
```

這邊安裝2.12是為了搭配tflearn通用版本


安裝tflearn
```
pip install tflearn
```


為了不要有相容性問題，這裡的Pillow要先卸載再降級
```
pip uninstall Pillow
```


安裝低版本，避免新版本不相容
```
pip install Pillow==9.5.0
```


安裝中文拆字器，他可以把 "我說明天吃什麼"，拆成 ["我","說","明天","吃","什麼"]，而不是 ["我","說明","天","吃","什麼"]
```
pip install jieba
```

安裝英文拆字器
```
pip install nltk
```

然後 numpy
```
pip install numpy
```

最後的Discord.py
```
pip install -U discord.py
```

# 初次使用
要先去Discord.py最後一行的token要改成自己的機器人token
Discord.py 中的 Creator 變數是開發者，可以改成自己的名字
Discord.py 中的 BotName 變數是機器人的名稱，可以添加

然後Process_Output.py BirthDay參數自己改，那是機器人的生日

在intents.json有機器人的所有反應跟資料庫，tag數要自己疊加，然後我有提供幾個參數

| 參數  | 參數意義 |
| ------------- | ------------- |
| {__BOT_NAME}  | 機器人名稱  |
| {__NOW_TIME}  | 現在時間  |
| {__FOOD_DATABASE}  | 隨機的食物資料庫  |
| {__CREATOR_NAME}  | 製作者名稱  |
| {__DICE}  | 六面骰子  |
| {__AGE}  | 機器人年齡  |
| {__BIRTHDAY}  | 機器人生日  |
| {__UNKNOW_REPLY}  | 這個是機器人不知道說啥時會用的，基本上不應該出現在intents.json  |

# 最後
```
py .\Discord.py
```
開始你的旅程吧，孩子

然後觸發方式就是在某個機器人可以講話跟看到的地方輸入 "機器人名稱" + "你要說的內容"

以上，之後還會更新。
