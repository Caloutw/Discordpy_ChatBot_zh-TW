# Discordpy_ChatBot_zh-TW
A Chatbot AI Project with Tensorflow

Python新手，程式碼真的是東拼西湊，請見諒

這是基於 Tensorflow 和 Keith Flagg 提供之原始碼開發的AI神經網路回應機器人

因為之前被BrainJS搞了，所以打算找一個可以GPU加速的身經網路學習框架

阿好死不死公司電腦沒有NVDIA卡，沒辦法玩Pytorch，所以只能退而求其次搞個Python

反正這東西內顯也可以加速，嗚呼~

# 安裝、開始使用
必要插件有 Tensorflow、numpy、tflearn、nltk、jieba

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

安裝中文拆字器，他可以把"我說明天吃什麼"，拆成["我","說","明天","吃","什麼"]，而不是["我","說明","天","吃","什麼"]
```
pip install jieba
```
