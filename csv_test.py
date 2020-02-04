# c03.csvからデータを辞書に入れて計算をするクラスを作成
#csvを読み込んで出力する
import csv
file_path = "c03.csv"


# クラスを作成して都道府県を入力すると女性の人口の合計値がでるようにする
class Sum_anser:
    def __init__(self,place):
        self.name = place

    def out_text(self):
        return self.name

    def print_out(self):
        with open(file_path, newline='', encoding='shift_jis') as csvfile:
            kekka = 0
            reader = csv.DictReader(csvfile)
            for row in reader:
              todofuken = row['都道府県名']
              if todofuken == self.name:
                kekka += int(row['人口（女）'])
        return kekka
# それぞれをインスタンス化して結果を出力
hokkaido = Sum_anser('北海道')
print(hokkaido.print_out())
akita = Sum_anser('秋田県')
print(akita.print_out())
