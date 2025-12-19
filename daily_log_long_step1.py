from datetime import datetime

def count_today_entries(lines, today):
    """
    今日のヘッダー以降にある「ログ行の数」を数えて返す関数
    """
    count = 0
    found_today = False

    for line in lines:
        if line.strip() == f"--- {today} ---":
            found_today = True
            count = 0
            continue
        if found_today:
            if line.strip() != "":
                count += 1

    return count


# 今日の日付（例：2025-11-23）
today = datetime.now().strftime("%Y-%m-%d")

# ログファイルを全部読む（なければ空）
try:
    with open("daily_log.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        content = "".join(lines)
except FileNotFoundError:
    lines = []
    content = ""

# 今日の日付のヘッダーがなければ追加する
with open("daily_log.txt", "a", encoding="utf-8") as f:
    if f"--- {today} ---" not in content:
        f.write(f"--- {today} ---\n")

# 今日のヘッダー以降の行数を数えて「回数」を決める（関数を使用）
count = count_today_entries(lines, today)

# ★ ここを追加（ターミナルに「今日の総回数」を表示）★
print(f"（情報）今日の記録は、これで合計 {count + 1} 回目です。")

# メッセージ入力
message = input("ログに書き込むメッセージを入力してください：")

# 現在時刻（例：2025-11-23 18:25）
now = datetime.now().strftime("%Y-%m-%d %H:%M")

# ログ書き込み（回数つき）
with open ("daily_log.txt", "a", encoding="utf-8") as f:
    f.write(f"{count + 1}回目: {now}: {message}\n")

print("ログに書き込みました！")
