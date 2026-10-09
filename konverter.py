import requests
import json
import os
from datetime import datetime


FILE_DATA = "data_mata_uang.json"


def muat_data():
    if os.path.exists(FILE_DATA):
        with open(FILE_DATA, "r") as f:
            return json.load(f)
    else:
        return {}


def simpan_data(data):
    with open(FILE_DATA, "w") as f:
        json.dump(data, f, indent=2)


def tampilkan_menu():
    print()
    print("╔══════════════════════════════════════════╗")
    print("║    💰 SISTEM MANAJEMEN MATA UANG 💰     ║")
    print("╠══════════════════════════════════════════╣")
    print("║  [1] Tambah Mata Uang Baru               ║")
    print("║  [2] Lihat Daftar Mata Uang              ║")
    print("║  [3] Update Nilai Tukar                  ║")
    print("║  [4] Konversi Mata Uang                  ║")
    print("║  [5] Hapus Mata Uang                     ║")
    print("║  [6] Simpan & Keluar                     ║")
    print("╚══════════════════════════════════════════╝")


def tambah_mata_uang(data):
    print("\n\n------Tambah mata uang baru------")
    kode = input("Kode mata uang(cnth:IDR): ").strip().upper()

    if kode in data:
        print(f"Kode {kode} sudah ada")
        return
    nama = input("input mata uang(cnth:rupiah indonesia): ").strip()
    simbol = input("simbol(cnth:Rp): ").strip()

    while True:
        try:
            nilai = float(input("Nilai tukar terhadap 1 USD (cth: 15800): "))
            if nilai <= 0:
                raise ValueError
            break
        except ValueError:
            print("Harus angka positif")

    data[kode] = {
        "nama": nama,
        "simbol": simbol,
        "nilai_tukar": nilai,
        "tanggal_dibuat": datetime.now().isoformat(),
    }
    simpan_data(data)
    print(f"✅ {nama} ({kode}) berhasil ditambahkan!")


def lihat_daftar(data):
    print("\n -----daftar mata uang-----")

    if not data:
        print("\n Belum ada mata uang. tambahkan dahulu!!!")
        return
    print(f"{'Kode':<8} {'Nama':<25} {'Simbol':<8} {'1 USD ='}")
    print("─" * 55)

    for kode, info in data.items():
        print(
            f"{kode:<8} {info['nama']:<25} {info['simbol']:<8} {info['nilai_tukar']:,.2f}"
        )


def update_nilai_tukar(data):
    print("\n-----Update nilai tukar-----")

    kode = input("Input mata uang: ").strip().upper()

    if kode not in data:
        print(f"\n Kode {kode} tidak ditemukan!")
        return

    info = data[kode]
    print(f"  {info['nama']} ({kode})")
    print(
        f"  Nilai tukar saat ini: 1 USD = {info['simbol']}{info['nilai_tukar']:,.2f}"
    )

    while True:
        try:
            baru = float(input("Nilai tukar baru terhadap 1 USD: "))
            if baru <= 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Harus angka positif!")

    lama = info["nilai_tukar"]
    data[kode]["nilai_tukar"] = baru
    simpan_data(data)
    print(f"✅ {kode}: {lama:,.2f} → {baru:,.2f}")


def konversi_mata_uang(data):
    print("\n── Konversi Mata Uang ──")
    asal = input("Dari kode mata uang: ").upper().strip()
    if asal not in data:
        print(f"❌ Kode '{asal}' tidak ditemukan!")
        return

    tujuan = input("Ke kode mata uang  : ").upper().strip()
    if tujuan not in data:
        print(f"❌ Kode '{tujuan}' tidak ditemukan!")
        return

    while True:
        try:
            jumlah = float(input(f"Jumlah {asal}: "))
            if jumlah <= 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Harus angka positif!")

    rate_asal = data[asal]["nilai_tukar"]
    rate_tujuan = data[tujuan]["nilai_tukar"]
    hasil = jumlah * (rate_tujuan / rate_asal)

    simbol_asal = data[asal]["simbol"]
    simbol_tujuan = data[tujuan]["simbol"]
    print(
        f"\n  💱 {simbol_asal}{jumlah:,.2f} {asal} = {simbol_tujuan}{hasil:,.2f} {tujuan}"
    )


def hapus_mata_uang(data):
    print("\n── Hapus Mata Uang ──")
    kode = input("Kode mata uang: ").upper().strip()
    if kode not in data:
        print(f"❌ Kode '{kode}' tidak ditemukan!")
        return

    info = data[kode]
    print(f"  {info['nama']} ({kode}) - {info['simbol']}")

    konfirmasi = input("Yakin hapus? (y/n): ").lower()
    if konfirmasi != "y":
        print("Dibatalkan.")
        return

    del data[kode]
    simpan_data(data)
    print(f"✅ {kode} berhasil dihapus!")


def main():
    data = muat_data()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu [1-6]: ").strip()
        if pilihan == "1":
            tambah_mata_uang(data)
        elif pilihan == "2":
            lihat_daftar(data)
        elif pilihan == "3":
            update_nilai_tukar(data)
        elif pilihan == "4":
            konversi_mata_uang(data)
        elif pilihan == "5":
            hapus_mata_uang(data)
        elif pilihan == "6":
            simpan_data(data)
            print("\n👋 Terima kasih! Data tersimpan.")
            break
        else:
            print("❌ Pilihan tidak valid! Masukkan angka 1-6.")


if __name__ == "__main__":
    main()
