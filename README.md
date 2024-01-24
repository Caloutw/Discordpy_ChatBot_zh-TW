# Discordpy_ChatBot_zh-TW
A Chatbot AI Project with Tensorflow
Python新手，程式碼真的是東拼西湊，請見諒
基於 Tensorflow 和 Keith Flagg 提供之原始碼開發的AI神經網路回應機器人

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
