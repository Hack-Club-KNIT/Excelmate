
# import openpyxl
import time
from colors import bcolors
# wb = openpyxl.load_workbook('Input.xlsx')
# sheet = wb.get_sheet_by_name('Sheet1')
print(bcolors.BOLD+bcolors.HEADER+"----------------------Excelmate-----------------"+bcolors.ENDC+bcolors.ENDC)
for x in range(0,101,5):
    print(bcolors.OKGREEN+"Loading...."+str(x)+"%"+bcolors.ENDC)
    time.sleep(0.25)

print(bcolors.FAIL+"---Project still under development---\n"+bcolors.ENDC)
time.sleep(1)
print(bcolors.WARNING+"Willing to contribute join us on Discord or make pull request."+bcolors.ENDC)

# wb.save("Output.xlsx")