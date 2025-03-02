import random

class Player:
    STONE = 0    # グー
    SCISSORS = 1 # チョキ
    PAPER = 2    # パー

    def __init__(self, name):
        self.name = name
        self.win_count = 0

    def show_hand(self):
        hand = random.randint(0, 2)
        return hand

    def notify_result(self, result):
        if result:
            self.win_count += 1

    def get_win_count(self):
        return self.win_count

    def get_name(self):
        return self.name


class Judge:
    def start_janken(self, player1, player2):
        print("【ジャンケン開始】\n")

        for cnt in range(3):
            print(f"【{cnt + 1}回戦目】")
            winner = self.judge_janken(player1, player2)

            if winner:
                print(f"\n{winner.get_name()}が勝ちました!\n")
                winner.notify_result(True)
            else:
                print("\n引き分けです！\n")

        print("【ジャンケン終了】\n")
        final_winner = self.judge_final_winner(player1, player2)
        print(f"{player1.get_win_count()} 対 {player2.get_win_count()}で")
        if final_winner:
            print(f"{final_winner.get_name()}の勝ちです！\n")
        else:
            print("引き分けです！\n")

    def judge_janken(self, player1, player2):
        player1_hand = player1.show_hand()
        player2_hand = player2.show_hand()

        self.print_hand(player1_hand)
        print(" vs. ", end="")
        self.print_hand(player2_hand)
        print("\n")

        if ((player1_hand == Player.STONE and player2_hand == Player.SCISSORS) or
            (player1_hand == Player.SCISSORS and player2_hand == Player.PAPER) or
            (player1_hand == Player.PAPER and player2_hand == Player.STONE)):
            return player1
        elif ((player1_hand == Player.STONE and player2_hand == Player.PAPER) or
              (player1_hand == Player.SCISSORS and player2_hand == Player.STONE) or
              (player1_hand == Player.PAPER and player2_hand == Player.SCISSORS)):
            return player2
        else:
            return None

    def judge_final_winner(self, player1, player2):
        if player1.get_win_count() > player2.get_win_count():
            return player1
        elif player1.get_win_count() < player2.get_win_count():
            return player2
        else:
            return None

    def print_hand(self, hand):
        if hand == Player.STONE:
            print("グー", end="")
        elif hand == Player.SCISSORS:
            print("チョキ", end="")
        elif hand == Player.PAPER:
            print("パー", end="")
        else:
            print("不明", end="")


if __name__ == "__main__":
    saito = Judge()
    murata = Player("村田さん")
    yamada = Player("山田さん")
    saito.start_janken(murata, yamada)
