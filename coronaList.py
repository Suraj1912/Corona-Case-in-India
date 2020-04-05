import xlsxwriter, requests, bs4

def corona_fun():
    state = []
    positveCases = []
    cured = []
    death = []

    r = requests.get('https://www.mohfw.gov.in/')
    data = r.text
    # print(data)
    soup = bs4.BeautifulSoup(data, 'html.parser')

    getStr = ''
    for tr in soup.find_all('tbody')[-1].find_all('tr'):
        getStr += tr.get_text()

    getStr = getStr[1:]
    itemList = getStr.split('\n\n')
    # print(itemList)
    for item in itemList[:30]:
        dataList = item.split('\n')
        # print(dataList)
        state.append(dataList[1])
        positveCases.append(dataList[2])
        cured.append(dataList[3])
        death.append(dataList[4])

    workbook = xlsxwriter.Workbook('Corona Cases in India.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'States')
    worksheet.write('B1', 'Positive Cases')
    worksheet.write('C1', 'Cured')
    worksheet.write('D1', 'Death')

    for i in range(2, 32):
        ws1 = 'A' + str(i)
        ws2 = 'B' + str(i)
        ws3 = 'C' + str(i)
        ws4 = 'D' + str(i)
        worksheet.write(ws1, state[i-2])
        worksheet.write(ws2, positveCases[i-2])
        worksheet.write(ws3, cured[i-2])
        worksheet.write(ws4, death[i-2])

    l = [int(i) for i in positveCases]
    total_pc = sum(l)

    l1 = [int(i) for i in cured]
    total_cured = sum(l1)

    l2 = [int(i) for i in death]
    total_death = sum(l2)

    worksheet.write('A33', 'Total Positive cases')
    worksheet.write('B33', str(total_pc))
    worksheet.write('A34', 'Total Cured')
    worksheet.write('B34', str(total_cured))
    worksheet.write('A35', 'Total Death')
    worksheet.write('B35', str(total_death))
    workbook.close()