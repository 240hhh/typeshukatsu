def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    i = 0
    j = len(array)-1
    #  smallに基準値未満の要素を、largeに基準値以上の要素を格納
    small = []
    large = []
    while i <= j:
        # 先頭から、基準値以上の要素が見つかるまで探索
        if array[i] < pivot:
            small.append(array[i])
            i += 1
            continue
        # 末尾から、基準値未満の要素が見つかるまで探索
        elif array[j] >= pivot:
            large.insert(0,array[j])
            j -= 1
            continue
        #　上の探索で見つかった要素どうしを交換し、リストに格納
        else:
            small.append(array[j])
            large.insert(0,array[i])
            i +=1
            j -=1

    #　リストの先頭が最小値の場合、ソートが無限ループするので、先頭の要素でリスト分割
    if len(small)==0:
        small = large[:1]
        large = large[1:]

    #　再帰的処理
    small = sort(small)
    large = sort(large)
    return small + large

    # ここまで記述

if __name__ == '__main__':
    main()
