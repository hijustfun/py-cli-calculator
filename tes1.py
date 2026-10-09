import tes2

nama = input("masukkan namamu: ")
umur = tes2.akhir_file()

konfirmasi = input(f"Hai, apa benar nama kamu: {nama}\ndan kamu berusia: {umur}\ny/n? ").lower().strip()
if konfirmasi == "y":
	print("silakan masuk")
elif konfirmasi == "n":
	print("silakan input ulang")
else:
	print("masukkan 'y' atau 'n'. Terima kasih :)")
