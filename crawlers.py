import requests
from bs4 import BeautifulSoup
import csv
import time


class Crawlers:

    def __init__(self, n4_url, n3_url, n4_file_name, n3_file_name):
        self.n4_url = n4_url
        self.n3_url = n3_url
        self.n4_file_name = n4_file_name
        self.n3_file_name = n3_file_name

    def n4_number_get(self, url, file_name):
        data = []
        num, all_number = self.bs(url)
        for td in range(3, (all_number//344)+5):
            tmp = num[td].text.replace('.', '')
            for i in range(0, len(str(tmp)), 4):
                try:
                    int(tmp[i:i+4])
                    data.append(tmp[i:i+4])
                except:
                    pass
        
        self.write_csv(data, file_name, 4)

    def n3_number_get(self, url, file_name):
        data = []
        num, all_number = self.bs(url)
        for td in range(3, (all_number//275)+4):
            tmp = num[td].text.replace('.', '')
            for i in range(0, len(str(tmp)), 3):
                try:
                    int(tmp[i:i+3])
                    data.append(tmp[i:i+3])
                except:
                    pass

        self.write_csv(data, file_name, 3)

    def bs(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        html = BeautifulSoup(r.content, 'html.parser')
        num = soup.find_all('table')
        all_number = int(str(html.find_all('td')[6])[40:44])

        return num, all_number

    def write_csv(self, data, file_name, index:int):
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            if index == 4:
                writer.writerow(['index', 'num', 'num1', 'num2', 'num3', 'num4'])

                for i, column in enumerate(data):
                    num1 = column[0]
                    num2 = column[1]
                    num3 = column[2]
                    num4 = column[3]
                    writer.writerow([i+1, column, num1, num2, num3, num4])

            elif index == 3:
                writer.writerow(['index', 'num', 'num1', 'num2', 'num3'])
            
                for i, column in enumerate(data):
                    num1 = column[0]
                    num2 = column[1]
                    num3 = column[2]
                    writer.writerow([i+1, column, num1, num2, num3])

if __name__ == '__main__':
    n4_url = 'http://www.toe.jp/numbers34/n4/code.htm'
    n3_url = 'http://www.toe.jp/numbers34/n3/code.htm'

    n4_file_name = 'lotto4.csv'
    n3_file_name = 'lotto3.csv'
    clawlers = Crawlers(n4_url, n3_url, n4_file_name, n3_file_name)

    clawlers.n4_number_get(n4_url, n4_file_name)
    time.sleep(3)
    clawlers.n3_number_get(n3_url, n3_file_name)

