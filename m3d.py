import os, sys

print ("\033[1;32mIsilah Username & Password")
print ("\033[1;32mKalau gtw wa gw :v 081353398031")
username = 'm3d'
password = 'Gans'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("Username : ")
	if uname == username:
		pwd = raw_input("Password : ")

		if pwd == password:
			print "\n\033[1;34mHallo Selamat Datang di Tools BangZat", 
			sys.exit()

		else:
			print "\n\033[1;36mMaaf Password Salah\033[00m"
			print "Log in Kembali\n"
			restart()

	else:
		print "\n\033[1;36mMaaf Username Salah\033[00m"
		print "Log in Kembali\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
