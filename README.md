
## 開発したもの 

目的：仮想空間(メタバース)上で音声通話をしながらコミュニケーションができるアプリで、「病気や障がいなどがきっかけで感じる孤独感を軽減したい」という目的でミニマムで開発を進めました。

[紹介記事](https://kimikou-blog.jp/prototypes/vr%e3%82%a2%e3%83%97%e3%83%aa/)

## 利用ツール：Unity、Django、Express、React

 [VR_Interaction_UnityOpenXR(Unity)](https://github.com/NK-kimiya/VR_Interaction_UnityOpenXR)　

 [VR_Interaction_API(Django)](https://github.com/NK-kimiya/VR_Interaction_API)　

 [VR_Interaction_signallingserver(Express)](https://github.com/NK-kimiya/VR_Interaction_signallingserver)　

 [VR_Interaction_WebRTC(React)](https://github.com/NK-kimiya/VR_Interaction_WebRTC)　

 ※下記の方法での実行を試しました。　
 
 Django、Express、Reactはホスティングサービス(RenderやHerokuなど)でホスティングを行い、Unityはビルドし、MetaQuest2に実行ファイルを送信　

---

## 🧩 Djangoプロジェクトの機能概要

このDjangoプロジェクトは、Unity側のVRアバター操作やユーザー管理と連携するための**シンプルな認証・情報取得用APIサーバー**です。  
ユーザー情報（名前・パスワード・ID・アバター番号）を扱い、UnityからのAPIリクエストに応じてデータを返す機能を備えています。

---

### ✅ 実装されている主な機能

#### 🔹 カスタムユーザーモデル（`CustomModel`）

| フィールド        | 内容                                           |
|------------------|------------------------------------------------|
| `name`           | ユーザー名（ユニーク）                         |
| `_password`      | ハッシュ化されたパスワード                     |
| `id`             | 自動生成される10桁の一意なID                   |
| `avatar_number`  | ユーザーに割り当てられたアバター番号（初期値0）|

- 保存時にパスワードを自動的にハッシュ化
- `check_password()` メソッドにより照合可能

---

### ✅ 実装API一覧（`views.py`）

| HTTPメソッド | エンドポイント               | 機能概要                                                             |
|--------------|-------------------------------|----------------------------------------------------------------------|
| `POST`       | `/api/get-name-id/`           | `name` と `password` から一致するユーザーを検索し、`id` と `avatar_number` を返す |
| `POST`       | `/api/get-entry-by-id/`       | `id` を受け取り、該当ユーザー情報をJSONで返す（エラーハンドリング付き） |

---

### 📦 使用ライブラリ・技術スタック

- **Django**：Webアプリケーションフレームワーク
- **Django REST Framework**：API構築のためのシリアライザー・汎用ビュー
- **make_password / check_password**：パスワードの安全なハッシュ化・検証
- **UUID / random**：ユニークなユーザーIDの生成処理

---


## 🔗 関連プロジェクト

・Djangoプロジェクトは、デプロイをすることで以下のUnityプロジェクトと連携して動作します。

📁 [VR_Interaction_UnityOpenXR(Unity)](https://github.com/NK-kimiya/VR_Interaction_UnityOpenXR)

- Meta Quest 2 向けにOpenXRを使用したVRアプリ
- Unity上のアバター操作・ネットワーク接続・認証情報の取得などを行います
- 本プロジェクトのAPI（Django）は、**ユーザーID取得やアバター番号の提供**を担当しています

・以下のReactプロジェクトとも連携して動作します。　

📁 [VR_Interaction_WebRTC(React)](https://github.com/NK-kimiya/VR_Interaction_WebRTC)　

-ユーザーを新規作成して、IDと使用するアバターの紐づけ　
-WebRTCWeb上で、音声通話とビデオ通話を行う

・以下のExpressプロジェクトも関連しています。　

📁 [VR_Interaction_signallingserver(Express)](https://github.com/NK-kimiya/VR_Interaction_signallingserver)　　

-ReactプロジェクトでWebRTCを実装する際のシグナリングサーバー





