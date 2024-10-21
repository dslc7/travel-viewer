# Travel Viewer

## 使い方

WebSocket サーバーを立て、最初の画面でサーバーの URL を入力して接続してください（デフォルトは`ws://localhost:9999`）。

サーバーからは以下のスキーマに則った JSON データを送信することで、画像の表示を切り替えできます。
新しいデータを受け付けるたびに、以前の表示はすべて消え、新しいデータが描画されます。

```jsonc
[
  {
    "q": "", // String (optional), Google Mapsに渡すクエリ。この値があるときに地図を表示する
    "z": "", // String (optional), Google Mapsに渡す縮尺。デフォルトは15
    "imgUrl": "", // String (optional), 表示する画像のURL。この値があるときに画像を表示する
    "name": "", // String (required), 表示する名前
    "yomigana": "" // String (optional), 表示する読み仮名
  } // 最大4つまで、それ以降は表示されない
]
```

Google Map クエリ制御の参考サイト: [http://www.shurey.com/html/googlemaps.html](http://www.shurey.com/html/googlemaps.html)
