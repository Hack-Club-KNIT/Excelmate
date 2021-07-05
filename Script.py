# import openpyxl
import time
# wb = openpyxl.load_workbook('Input.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
print("------------------------Excelmate-----------------")
for x in range(0,100,5):
    print("Loading...."+str(x)+"%")
    time.sleep(0.25)

print("---Project still under development---\n")
time.sleep(1)
print("Willing to contribute join us on Discord or make pull request.")

# wb.save("Output.xlsx")