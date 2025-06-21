# Pokemon Card Monitor Bot (Email版)

13の通販サイトを5分おきに巡回し、ポケモンカードの「抽選」「予約」情報を検出したら
- Gmail経由でメール通知
- Googleカレンダーに予定追加

## 設定方法

### 1. Secrets に登録（Settings > Secrets and variables > Actions）

- EMAIL_ADDRESS：Gmailアドレス
- EMAIL_PASSWORD：アプリパスワード（16桁）
- EMAIL_TO_ADDRESS：通知を受け取りたいメールアドレス

### 2. Googleカレンダー連携

- credentials.json を用意（デスクトップアプリ用 OAuth）
- 最初の実行時に認証が走ります（token.pickleが生成される）

