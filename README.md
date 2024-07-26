# Djangoチュートリアル：投票アプリ
## Demos  
＊GIFの表示に時間がかかる場合があります。  
デモ1【個別記録の追加】  


デモ2【LLMによる月案（構成1-4）作成】  


デモ3【RAGによる月案（構成5）作成】  


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

