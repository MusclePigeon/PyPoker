import random

# カードクラスの作成
class Card():
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

def main():
    # スートと役の要素を追加
    suits=("c","h","d","s")

    role = ("High Card","One Pair","Two Pair","Three of a kind", "Straight", "Flash", "Full House", "Four Card", "Straight Flash", "Royal Flash")
    role_count = [0 for i in range(len(role))]

    # デッキの作成
    deck = [Card(i, j) for i in range(4) for j in range(1,14)]
    
    # while文を追加して役の出現確率を調べる
    cnt = 0
    while(cnt < 1000):
        cnt += 1

        # シャッフルして5枚ドローする
        random.shuffle(deck)
        card = deck[:5]

        # 数字とスートの抽出
        card_nums = [c.num for c in card]
        card_suits = [c.suit for c in card]

        # 数字の最大重複数
        num_duplicate = 0
        for s in set(card_nums):
            if num_duplicate < card_nums.count(s):
                num_duplicate = card_nums.count(s)

        # スートの最大重複数
        suit_duplicate = 0
        for s in set(card_suits):
            if suit_duplicate < card_suits.count(s):
                suit_duplicate = card_suits.count(s)

        # ストレートかどうか
        straight_flag = False

        # 数字をまたぐケース
        if 1 in card_nums and 10 in card_nums:
            card_nums.remove(1)
            card_nums.append(14)

        max_val = max(card_nums)
        min_val = min(card_nums)
        ave_val = (max_val + min_val) / 2

        if max_val - min_val == 4 and ave_val in card_nums and ave_val - 1 in card_nums and ave_val + 1 in card_nums:
            straight_flag = True

        # 役判定
        score = 0

        # One Pair
        if len(set(card_nums)) == 4 and num_duplicate ==2:
            score = 1
        # Two Pair
        elif len(set(card_nums)) == 3 and num_duplicate == 2:
            score = 2
        # Three of a kind
        elif len(set(card_nums)) == 3 and num_duplicate == 3:
            score = 3
        # Straight
        elif straight_flag == True and suit_duplicate !=5:
            score = 4
        # Flash
        elif suit_duplicate == 5 and straight_flag == False:
            score = 5
        # Full House
        elif len(set(card_nums)) == 2 and num_duplicate == 3:
            score = 6
        # Four Card
        elif len(set(card_nums)) == 2 and num_duplicate == 4:
            score = 7
        # Straight Flash
        elif straight_flag == True and suit_duplicate == 5:
            score = 8
            # Royal Flash
            if 14 in card_nums and 10 in card_nums:
                score = 9

        
        # 役の出現回数をカウントする
        role_count[score] += 1

        print('[{}]'.format(cnt), end=" ")
        for c in card:
            print('{}{}'.format(suits[c.suit], c.num), end=" ")
        print(role[score])
    
    # while分終わり

    # 実行結果
    print("-"*20)
    print(cnt, '回試行')
    print("-"*20)
    for i in range(len(role)):
        print('{}: {}回 確率:{}'.format(role[i], role_count[i], role_count[i]/cnt*100))


if __name__ == "__main__":
    main()