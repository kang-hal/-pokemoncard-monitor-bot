# Pokemon Card Monitor Bot

## 概要

13の通販サイトを5分おきに巡回し、ポケモンカードの「抽選」「予約」情報を検出したら
- LINE Notifyに通知
- Googleカレンダーに予定追加

を行う自動Botです。

## セットアップ手順

### 1. GitHubにこのリポジトリをインポート

このリポジトリをテンプレートとして「Use this template」から自分のアカウントに作成。

### 2. Secrets に登録する情報

GitHub上で以下を登録します：

- `LINE_TOKEN`：LINE Notifyのアクセストークン

### 3. Googleカレンダー連携の初回設定

1回目の実行時に、以下のファイルを手動で用意してください：

- `credentials.json`：Google APIで取得（デスクトップアプリ用）
- 実行時に認証画面が開き、`token.pickle`が自動生成されます

以降は自動実行されます。

