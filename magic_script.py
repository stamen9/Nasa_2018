import pandas as pd
import xlrd
import json

def main():
    file_names = []
    file_names.append('10m_temps_MORE_Dixon.xls')
    file_names.append('10m_temps_NSIDC_Dixon.xls')

    with open("all.json",'w') as f:
        data = []
        for name in file_names:
            xl = pd.ExcelFile(name)
            sheet = xl.parse(0)
            tempretures = dict(sheet["Temp"])
            data.append(list(tempretures.values()))
        json.dump(data,f)
    

if __name__ == "__main__":
    main()