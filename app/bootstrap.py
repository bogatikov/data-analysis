import pandas as pd
import matplotlib.pyplot as plt


def run():
    titanic = pd.read_csv('C:\\Users\\xiaomi\\telderiSiteData.csv')
    op = titanic['Оптимальная цена']
    op.plot(x="A", y='B')
    plt.show()
    # table = []
    # types = set()
    # map = dict()
    # prices = []
    # with open('C:\\Users\\xiaomi\\OneDrive\\Рабочий стол\\telderiSiteData.csv') as fin:
    #     reader = csv.reader(fin)
    #     for row in reader:
    #         if len(row) != 0:
    #             if (row[0] == 'Название'):
    #                 continue
    #             table.append(row)
    #             cnrted = str(row[2]).replace(" руб.", "").replace(" ", "")
    #             if cnrted != '':
    #                 integ = int(cnrted)
    #                 p = int(str(row[2]).replace(" руб.", "").replace(" ", ""))
    # prices.append(integ)
    # for s in str(row[1]).split("."):
    #     if s != '':
    #         n = map.get(s, 0)
    #         map[s] = n + 1
    #         types.add(s.strip())
    # print(max(prices))
    # print(min(prices))
    # print(len(prices))
    # print(sum(prices))
    # print(sum(prices)/len(prices))
    return None
