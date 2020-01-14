import getpass
from colorama import Fore
print("Pypass")
pin = getpass.getpass("Enter your pin: ")
if pin == "PIN HERE":
  passw = getpass.getpass("Enter your password: ")
  if passw == "PASSWORD HERE":
    print(Fore.GREEN + "Secret content")
  else:
    print("Wrong password.")
else:
  print("Wrong pin.")
