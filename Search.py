def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    min = -1
    max = len(sorted_array)
    while max-min > 1:
        n = int((min+max)/2)
        if  target_number < sorted_array[n]:
            max = n
        elif target_number > sorted_array[n]:
            min = n
        else:
            return n

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
