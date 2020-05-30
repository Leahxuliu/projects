import xlwings as xw
app=xw.App(visible=True,add_book=False)

wb=xw.Book()
sht=wb.sheets[0]
sht.range('a1').value="hello"
rng = sht.range("A1:A100")
rng.formula='=SUM(B1:B5)'
