cards_map = {
    "A": 1, "1": 1,
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 11, "11": 11,
    "Q": 12, "12": 12,
    "K": 13, "13": 13
}

while True:
    try:
        cards = input("請輸入 5 張卡牌（例如：A 10 K J Q），或輸入 quit/exit 結束遊戲: ").split()

        if cards[0].lower() in ['quit', 'exit']:
            print("程式結束，再見！")
            break

        if len(cards) == 5:
            cards_valid = []
            cards_invalid = []

            for i in cards:
                cards_upper = i.upper()
                if cards_upper in cards_map:
                    cards_valid.append(cards_map[cards_upper])
                else:
                    cards_invalid.append(cards_upper)

            if cards_invalid:
                raise ValueError(f"{', '.join(cards_invalid)} 等卡牌不存在，請重新輸入")
            else:
                cards_valid.sort(reverse=True)
                print(f"最高三張卡牌：{cards_valid[0:3]}")
                print(f"總和為：{sum(cards_valid[0:3])}")

        elif 0 <= len(cards) < 5:
            print(f"輸入的卡牌數量不夠，目前差 {5 - len(cards)} 張，請重新輸入")

        else:
            print(f"輸入的卡牌數量超過，目前多了 {len(cards) - 5} 張，請重新輸入")

    except ValueError as e:
        print("發生錯誤，", e)
