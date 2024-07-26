# Djangoチュートリアル：投票アプリ
## Demos    

**デモ1【個別記録の追加】**  
![チュートリアル_demo1](https://github.com/user-attachments/assets/e9d3a3a7-5451-43dd-b1a6-1a2196cc6723)  

**デモ2【LLMによる月案（構成1-4）作成】**  
![チュートリアル_demo2](https://github.com/user-attachments/assets/a9aa5cb1-5821-4e36-9598-06b04e079bd2)  

**デモ3【RAGによる月案（構成5）作成】**  
![チュートリアル_demo3](https://github.com/user-attachments/assets/1bd19117-b807-45c3-8bd4-0ee49afd7847)  

## 起動方法

### 1．任意のフォルダにレポジトリをクローン
` git clone https://github.com/tadano-dreamer/childcare_ragapp.git`  

### 2．必要なモジュールのインストール
＊仮想環境でインストールする場合は先に`python -m venv venv`をターミナルに入力  

-1 `cd childcare_ragapp`  
-2 `pip install -r requirements.txt`　

### 3. サーバを起動
＊事前準備として：  
　・chat/views.py 内にOpenAIのAPIキーを入力  
を行う  

ターミナルに以下を入力  
```
python manage.py runserver
```

`localhost:8000`でブラウザから挙動を確認

