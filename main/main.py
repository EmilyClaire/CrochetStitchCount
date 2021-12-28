
import file_logic.read_file as rf

try:
    rows = rf.read_file(input('Enter the path of the pattern .txt file to check:  '))

except BaseException as err:
    print('There was an error: ' + str(err))