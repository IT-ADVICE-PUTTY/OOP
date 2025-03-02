import random

# ジャンケンの手を表す定数
STONE = 0  # グー
SCISSORS = 1  # チョキ
PAPER = 2  # パー

def main():
    # 村田さんの勝ち数
    murata_win_count = 0

    # 山田さんの勝ち数
    yamada_win_count = 0

    # プログラム開始メッセージを表示する
    print("【ジャンケン開始】\n")

    # ジャンケンを３回実施する
    for cnt in range(3):
        # 何回戦目かを表示する
        print(f"【{cnt + 1}回戦目】")

        # 村田さんが何を出すか決める
        random_num = random.randint(0, 2)
        if random_num == 0:
            murata_hand = STONE
            print("グー", end="")
        elif random_num == 1:
            murata_hand = SCISSORS
            print("チョキ", end="")
        else:
            murata_hand = PAPER
            print("パー", end="")

        print(" vs. ", end="")

        # 山田さんが何を出すか決める
        yamada_hand = PAPER
        print("パー")

        # どちらが勝ちかを判定し、結果を表示する
        if (murata_hand == STONE and yamada_hand == SCISSORS) or \
           (murata_hand == SCISSORS and yamada_hand == PAPER) or \
           (murata_hand == PAPER and yamada_hand == STONE):
            print("\n村田さんが勝ちました！\n")
            murata_win_count += 1
        elif (murata_hand == STONE and yamada_hand == PAPER) or \
             (murata_hand == SCISSORS and yamada_hand == STONE) or \
             (murata_hand == PAPER and yamada_hand == SCISSORS):
            print("\n山田さんが勝ちました！\n")
            yamada_win_count += 1
        else:
            print("\n引き分けです！\n")

    # 最終的な勝者を判定し、画面に表示する
    print("【ジャンケン終了】\n")
    if murata_win_count > yamada_win_count:
        print(f"{murata_win_count}対{yamada_win_count}で村田さんの勝ちです！\n")
    elif murata_win_count < yamada_win_count:
        print(f"{murata_win_count}対{yamada_win_count}で山田さんの勝ちです！\n")
    else:
        print(f"{murata_win_count}対{yamada_win_count}で引き分けです！\n")

if __name__ == "__main__":
    main()
