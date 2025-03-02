import random

# ジャンケンの手を表す定数
STONE = 0  # グー
SCISSORS = 1  # チョキ
PAPER = 2  # パー

def main():
    # プレイヤー１の勝ち数
    player1_win_count = 0

    # プレイヤー２の勝ち数
    player2_win_count = 0

    # プログラム開始メッセージを表示する
    print("【ジャンケン開始】\n")

    # ジャンケンを３回実施する
    for cnt in range(3):
        # 何回戦目かを表示する
        print(f"【{cnt + 1}回戦目】")

        # プレイヤー１が何を出すか決める
        random_num = random.randint(0, 2)
        if random_num < 1:
            player1_hand = STONE
            print("グー", end="")
        elif random_num < 2:
            player1_hand = SCISSORS
            print("チョキ", end="")
        else:
            player1_hand = PAPER
            print("パー", end="")

        print(" vs. ", end="")

        # プレイヤー２が何を出すか決める
        random_num = random.randint(0, 2)
        if random_num < 1:
            player2_hand = STONE
            print("グー")
        elif random_num < 2:
            player2_hand = SCISSORS
            print("チョキ")
        else:
            player2_hand = PAPER
            print("パー")

        # どちらが勝ちかを判定し、結果を表示する
        if (player1_hand == STONE and player2_hand == SCISSORS) or \
           (player1_hand == SCISSORS and player2_hand == PAPER) or \
           (player1_hand == PAPER and player2_hand == STONE):
            print("\nプレイヤー１が勝ちました！\n")
            player1_win_count += 1
        elif (player1_hand == STONE and player2_hand == PAPER) or \
             (player1_hand == SCISSORS and player2_hand == STONE) or \
             (player1_hand == PAPER and player2_hand == SCISSORS):
            print("\nプレイヤー２が勝ちました！\n")
            player2_win_count += 1
        else:
            print("\n引き分けです！\n")

    # 最終的な勝者を判定し、画面に表示する
    print("【ジャンケン終了】\n")
    if player1_win_count > player2_win_count:
        print(f"{player1_win_count}対{player2_win_count}でプレイヤー１の勝ちです！\n")
    elif player1_win_count < player2_win_count:
        print(f"{player1_win_count}対{player2_win_count}でプレイヤー２の勝ちです！\n")
    else:
        print(f"{player1_win_count}対{player2_win_count}で引き分けです！\n")

if __name__ == "__main__":
    main()
