import getpass
from colorama import Fore, Style
print("2Password Password database")
pin = getpass.getpass("Enter your pin: ")
if pin == "PIN HERE":
  passw = getpass.getpass("Enter your password: ")
  if passw == "PASSWORD HERE":
    print("")
    print(Style.RESET_ALL + "Thing:", Fore.GREEN + "Password for the thing")
  else:
    print("Wrong password.")
else:
  print("Wrong pin.")
