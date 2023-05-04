from licensing.models import *
from licensing.methods import Key, Helpers
import tkinter as tk
from tkinter import ttk

RSAPubKey = "<RSAKeyValue><Modulus>w66wn9E/o2ibA2xPdsd28RnGwCt0eS9lj7P4NlZ1T/q6fDCAl8pYRkd69ScYMsOE+zhxY9/2Wg1Le9Fncbcl4+nDBWfv9uLAPh6svE9gIks3IRBpp+zEyiEGZpoX/pWOfGQjzeswBRWUN7J6AUgIfMZWvvfdSdjGvNx8czUJvwVM9tzx0npt0BazR62UDeNL2IW9iXZQ0fqRccQbXvBHMBmzJzAzE4LGT9W+j9bVpIA5wOT2ehlpiL2OxnLTv7Ug0FcU5aWG5GLdcDUSd7W2dBM/0WidihsAyu0FGPkATAuiuibo0QnBksSc2sZ9S1L2ci93YDhiX0p62HRhKs3Bqw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI0NjE4NDUwNSIsIkUxZ2VydktGaTN3MTlZWERxVHVFVzA3NzAzOVRWajhpSWw3akpFMHQiXQ=="

global license_type
global trial
license_type = None
trial = False

def end_auth():
	with open("current_license.txt", "w") as f:
		f.writelines([str(license_type), "\n", str(trial)])
		f.close()

def authenticate(label, key):
	global license_type, trial
	result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=19842, \
                   key=key.get(),\
                   machine_code=Helpers.GetMachineCode())

	if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
	    # an error occurred or the key is invalid or it cannot be activated
	    # (eg. the limit of activated devices was achieved)
	    label.configure(text=f"Invalid license: {result[1]}")
	else:
	    license_key = result[0]

	    if license_key.f3:
	    	license_type = "Basic"
	    elif license_key.f4:
	    	license_type = "Pro"
	    elif license_key.f5:
	    	license_type = "Ultimate"

	    if license_key.f2:
	    	trial = True

	    if license_key.f1:
	    	if trial:
	    		label.configure(text=f"Success! Your trial of {license_type} will expire {license_key.expires}\nYou may now close this window to proceed to the application.")
	    	else:
	    		label.configure(text=f"Success! Your {license_type} plan will expire {license_key.expires}\nYou may now close this window to proceed to the application.")
	    else:
	    	label.configure(text=f"Success! Your {license_type} plan will never expire.\nYou may now close this window to proceed to the application.")

	    end_auth()

def begin_auth():
	root = tk.Tk()

	lbl = tk.Label(root, text="Please enter your license key:")
	lbl.pack()

	key = tk.StringVar()
	keyEntered = ttk.Entry(root, text="License Key", textvariable=key)
	keyEntered.pack()

	btn = tk.Button(root, text="Authenticate", command=lambda: authenticate(lbl, key))
	btn.pack()

	root.mainloop()

with open("current_license.txt", "r") as f:
			f.readline()
			if f.readline() == 'None':
				begin_auth()
			f.close()
