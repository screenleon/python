# 讀取期交所的csv檔案，不正常。
# data = pd.read_csv('op1216.csv', 'coding=Big5', engine='python')

temp = ""

with open('op1216.csv') as fp:
    line = fp.readline()
    temp = line.replace(" ", "")
    line = fp.readline()           # ----------------------------- continue line 2
    line = fp.readline()
    while line:
        temp += line.replace(" ", "")
        line = fp.readline()

# print(temp)

with open('optest.csv', 'w') as fp:
    fp.write(temp)
