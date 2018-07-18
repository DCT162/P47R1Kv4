import os, sys

print ("\033[1;31mMasukan Id Sama Passwordny:)")
print ("\033[1;37;1mGa Tau? Chat Gw 085760193797\033[1;33m")
print ("\033[1;33m")
ID = 'P47R1K21'
Password = 'Batrik21'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("#ID : ")
	if uname == ID:
		pwd = raw_input("#Password : ")

		if pwd == Password:
			print "\n\033[1;34mHai Gaes Welcome To P47R1K21", 
			sys.exit()
     
		else:
			print "\n\033[1;36mPassword Salah Jancok !!!\033[00m"
			print "Login Lagi!!\n"
			restart()

	else:
		print "\n\033[1;36mID Salah Jancok !!!\033[00m"
		print "Login Lagi!!\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()