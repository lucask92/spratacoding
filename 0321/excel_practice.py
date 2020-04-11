
from openpyxl import Workbook

wb = Workbook()      # 워크북을 생성한다.
ws = wb.active       # 워크 시트를 얻는다.
ws['A1'] = 'Hello'   # A1에 'Hello' 값을 입력한다.
wb.save('test.xlsx') # 엑셀로 저장한다.