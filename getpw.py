from weblogic.security.internal import *
from weblogic.security.internal.encryption import *
import sys

encryptionService = SerializedSystemIni.getEncryptionService(".")
clearOrEncryptService = ClearOrEncryptedService(encryptionService)

passwd = "{AES}STRINGHERE"
plainpwd = passwd.replace("\\", "")
print "Plain Text password is: " + clearOrEncryptService.decrypt(plainpwd)
