from plyer import notification
import requests, bs4
import coronaList

def Notify(title, message):
    notification.notify(title, message, app_icon='C:\\Users\\Hp\\OneDrive\\Pictures\\corona.ico', timeout=5)

def request(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    # Notify('Suraj', 'Hi')

    getHTML = request('https://www.mohfw.gov.in/')

    soup = bs4.BeautifulSoup(getHTML, 'html.parser')

    getStr = ''
    for tr in soup.find_all('tbody')[-1].find_all('tr'):
        getStr += tr.get_text()

    getStr = getStr[1:]
    itemList = getStr.split("\n\n")
    # print(itemList[:30])

    # Looping to show only states which are in below list --> 
    # states = ['Maharashtra', 'Punjab', 'Gujarat', 'Delhi']
    # for item in itemList[0:30]:
    #     dataList = item.split("\n")
    #     if dataList[1] in states:
    #         nTitle = "cases of COVID-19"
    #         nText = f"{dataList[1]}\nTotal Confirmed cases : {dataList[2]}\nCured : {dataList[3]} Deaths : {dataList[4]}"
    #         Notify(nTitle, nText) 
    # # print(dataList)
    
    def fun():
        while True:
            inp = input("Enter state which want to know :").lower()
            if not inp.isdigit():
                for item in itemList[:30]:
                    dataList = item.split('\n')
                    ldata = dataList[1].lower()
                    if ldata == inp:
                        nTitle = "cases of COVID-19"
                        nText = f"{dataList[1]}\nTotal Confirmed cases : {dataList[2]}\nCured : {dataList[3]} Deaths : {dataList[4]}"
                        Notify(nTitle, nText) 
                    elif ldata[:3] == inp[:3]:
                        print(f'It must be {ldata}')
                break
            else:
                print("Enter appropriate input")
        
    fun()

    while True:
        inp1 = input("Want to know other state (Y/N): ")
        if inp1 == 'Y' or inp1 == 'y':
            fun()
        elif inp1 == 'N' or inp1 == 'n':
            inp11 = input('Do you want to download excel file of corona cases in india (Y/N): ')
            if inp11 == 'Y' or inp11 == 'y':
                coronaList.corona_fun()
                print('Downloaded successfully')
                break
            elif inp11 == 'N' or inp11 == 'n':
                break


