import math
def main():
    print("Start?")
    print("Y/N")
    sb = input("Input: ")
    if sb == "y" or "Y":
        Analisa()
    elif sb == "n" or "N":
        exit()
    else:
        print("Invalid input.")

def Analisa():
    nct = input("Nama Calon Terjamin: ")
    act = input("Alamat Calon Terjamin: ")
    jpbg = input("Surety Bond: ")
    jkb = int(input("Jumlah Kekayaan Bersih: Rp."))
    nj = int(input("Nilai Jaminan: Rp. "))
    print("\n")
    print("Nama Calon Terjamin: " + nct)
    print("Alamat Calon Terjamin: " + act)
    print("Surety Bond: " + jpbg)
    print(f"Jumlah Kekayaan Bersih: Rp. {jkb}")
    print(f"Nilai Jaminan: Rp. {nj}")
    print("======================")
    print("\tCharacter")
    print("======================\n")
    print("1. Lama Operasional Usaha")
    print("A. > 10 tahun")
    print("B. >= 5 tahun s/d <= 10 tahun")
    print("C. < 5 tahun\n")

    jawaban = input("Jawaban Anda: ")
    score = 0
    if jawaban == "a":
        score = 100 / 100 * 7
    elif jawaban == "b":
        score = 66.67 / 100 * 7
    elif jawaban == "c":
        score = 33.33 / 100 * 7
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup = math.ceil(score * 10000)/10000
    print(f"Score untuk pertanyaan pertama: {rup}")
    print("====================================\n")

    print("2. Hubungan dengan Obligee")
    print("A. >2 Obligee")
    print("B. 2 Obligee")
    print("C. 1 Obligee\n")

    jawaban = input("Jawaban Anda: ")
    score1 = 0
    if jawaban == "a":
        score1 = 100 / 100 * 7
    elif jawaban == "b":
        score1 = 66.67 / 100 * 7
    elif jawaban == "c":
        score1 = 33.33 / 100 * 7
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup1 = math.ceil(score1 * 10000)/10000
    print(f"Score untuk pertanyaan kedua: {rup1}")
    print("====================================\n")

    print("3. Lama Berhubungan dengan Obligee")
    print("A. > 5 tahun")
    print("B. >= 2 tahun s/d <= 5 tahun")
    print("C. < 2 tahun\n")

    jawaban = input("Jawaban Anda: ")
    score2 = 0
    if jawaban == "a":
        score2 = 100 / 100 * 7
    elif jawaban == "b":
        score2 = 66.67 / 100 * 7
    elif jawaban == "c":
        score2 = 33.33 / 100 * 7
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup2 = math.ceil(score2 * 10000)/10000
    print(f"Score untuk pertanyaan ketiga: {rup2}")
    print("====================================\n")

    print("4. Indemnity Agreement")
    print("A. Oleh Direktur Utama")
    print("B. Oleh Surat Kuasa Direktur Utama\n")

    jawaban = input("Jawaban Anda: ")
    score3 = 0
    if jawaban == "a":
        score3 = 100 / 100 * 5
    elif jawaban == "b":
        score3 = 50 / 100 * 5
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup3 = math.ceil(score3 * 10000)/10000
    print(f"Score untuk pertanyaan keempat: {rup3}")
    print("====================================\n")

    print("5. Legalitas Indemnity Agreement")
    print("A. Notariil")
    print("B. Bermaterai dan Non Notarii")
    print("C. Tidak Bermaterai dan Non Notarii\n")

    jawaban = input("Jawaban Anda: ")
    score4 = 0
    if jawaban == "a":
        score4 = 100 / 100 * 5
    elif jawaban == "b":
        score4 = 66.67 / 100 * 5
    elif jawaban == "c":
        score4 = 33.33 / 100 * 5
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup4 = math.ceil(score4 * 10000)/10000
    print(f"Score untuk pertanyaan kelima: {rup4}")
    print("====================================\n")


    total_score = score + score1 + score2 + score3 + score4
    print(f"Total Score: {total_score}" + "%\n")

    print("======================")
    print("\tCapital")
    print("======================\n")
    print("1. Ratio Likuiditas Keuangan (Aktiva Lancar / kewajiban Lancar")
    print("A. > 100%")
    print("B. 80% < RL <= 100% ")
    print("C. <=80%\n")

    jawaban = input("Jawaban Anda: ")
    score5 = 0
    if jawaban == "a":
        score5 = 100 / 100 * 5
    elif jawaban == "b":
        score5 = 66.67 / 100 * 5
    elif jawaban == "c":
        score5 = 33.33 / 100 * 5
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup5 = math.ceil(score5 * 10000)/10000
    print(f"Score untuk pertanyaan pertama: {rup5}")
    print("====================================\n")

    print("2. Ratio Rentabilitas (Laba Rugi Tahun Berjalan / Ekuitas)")
    print("A. >15%")
    print("B. 10% < RR <= 15%")
    print("C. <= 10%\n")

    jawaban = input("Jawaban Anda: ")
    score6 = 0
    if jawaban == "a":
        score6 = 100 / 100 * 5
    elif jawaban == "b":
        score6 = 66.67 / 100 * 5
    elif jawaban == "c":
        score6 = 33.33 / 100 * 5
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup6 = math.ceil(score6 * 10000)/10000
    print(f"Score untuk pertanyaan kedua: {rup6}")
    print("====================================\n")

    print("3. Ratio Solvabilitas (Total Kewajiban / Ekuitas")
    print("A. <= 30%")
    print("B. 30% < RS <= 60% ")
    print("C. > 60%\n")

    jawaban = input("Jawaban Anda: ")
    score7 = 0
    if jawaban == "a":
        score7 = 100 / 100 * 5
    elif jawaban == "b":
        score7 = 66.67 / 100 * 5
    elif jawaban == "c":
        score7 = 33.33 / 100 * 5
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup7 = math.ceil(score7 * 10000)/10000
    print(f"Score untuk pertanyaan ketiga: {rup7}")
    print("====================================\n")

    print("4. Ekuitas vs Nilai Proyek sekarang")
    print("A. > 50%")
    print("B. > 25% s/d <= 50%")
    print("C. <= 25%\n")

    jawaban = input("Jawaban Anda: ")
    score8 = 0
    if jawaban == "a":
        score8 = 100 / 100 * 5
    elif jawaban == "b":
        score8 = 66.67 / 100 * 5
    elif jawaban == "c":
        score8 = 33.33 / 100 * 5
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup8 = math.ceil(score8 * 10000)/10000
    print(f"Score untuk pertanyaan keempat: {rup8}")
    print("====================================\n")

    print("5. Audit Laporan Keungan")
    print("A. Auditor Terdaftar")
    print("B. Non Audit")
    print("C. -\n")

    jawaban = input("Jawaban Anda: ")
    score9 = 0
    if jawaban == "a":
        score9 = 100 / 100 * 5
    elif jawaban == "b":
        score9 = 66.67 / 100 * 5
    elif jawaban == "c":
        score9 = 33.33 / 100 * 5
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup9 = math.ceil(score9 * 10000)/10000
    print(f"Score untuk pertanyaan kelima: {rup9}")
    print("====================================\n")

    print("6. Sumber Dana Pelaksanaan Pekerjaan")
    print("A. Modal Sendiri dan dari pihak luar*")
    print("B. Modal Sendiri")
    print("C. Pihak Luar*\n")
    print("* Fasilitas Perbankan/LKNB/KPBU/Crowd Funding/Investor DN/Asing\n")

    jawaban = input("Jawaban Anda: ")
    score10 = 0
    if jawaban == "a":
        score10 = 100 / 100 * 5
    elif jawaban == "b":
        score10 = 66.67 / 100 * 5
    elif jawaban == "c":
        score10 = 33.33 / 100 * 5
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup10 = math.ceil(score10 * 10000)/10000
    print(f"Score untuk pertanyaan keenam: {rup10}")
    print("====================================\n")

    total_score1 = score5 + score6 + score7 + score8 + score9 + score10
    print(f"Sub Total Nilai Capital: {total_score1}" + "%")

    print("======================")
    print("\tCapacity")
    print("======================\n")

    print("1. Pengalaman Terhadap Jenis Pekerjaan")
    print("A. > 4 proyek yang sama")
    print("B. > 1 s/d <= 4 proyek yang sama")
    print("C. Belum pernah\n")

    jawaban = input("Jawaban Anda: ")
    score11 = 0
    if jawaban == "a":
        score11 = 100 / 100 * 7
    elif jawaban == "b":
        score11 = 66.67 / 100 * 7
    elif jawaban == "c":
        score11 = 33.33 / 100 * 7
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup11 = math.ceil(score11 * 10000)/10000
    print(f"Score untuk pertanyaan pertama: {rup11}\n")

    print("2. Tenaga Ahli sesuai proyek")
    print("A. > 5 tenaga ahli")
    print("B. >= 2 s/d <= 5 tenaga ahli")
    print("C. < 2 tenaga ahli\n")

    jawaban = input("Jawaban Anda: ")
    score12 = 0
    if jawaban == "a":
        score12 = 100 / 100 * 3
    elif jawaban == "b":
        score12 = 66.67 / 100 * 3
    elif jawaban == "c":
        score12 = 33.33 / 100 * 3
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup12 = math.ceil(score12 * 10000)/10000
    print(f"Score untuk pertanyaan kedua: {rup12}")
    print("====================================\n")

    print("3. Proyek Lain Yang Sedang Dikerjakan")
    print("A. Tidak ada")
    print("B. s/d 2 proyek")
    print("C. > 2 proyek\n")

    jawaban = input("Jawaban Anda: ")
    score13 = 0
    if jawaban == "a":
        score13 = 100 / 100 * 5
    elif jawaban == "b":
        score13 = 66.67 / 100 * 5
    elif jawaban == "c":
        score13 = 33.33 / 100 * 5
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup13 = math.ceil(score13 * 10000)/10000
    print(f"Score untuk pertanyaan ketiga: {rup13}")
    print("====================================\n")

    print("4. Peralatan Untuk Mengerjakan Proyek")
    print("A. Cukup, Milik sendiri")
    print("B. Milik sendiri dan sewa")
    print("C. Sewa/renacan sewa\n")

    jawaban = input("Jawaban Anda: ")
    score14 = 0
    if jawaban == "a":
        score14 = 100 / 100 * 5
    elif jawaban == "b":
        score14 = 66.67 / 100 * 5
    elif jawaban == "c":
        score14 = 33.33 / 100 * 5
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup14 = math.ceil(score14 * 10000)/10000
    print(f"Score untuk pertanyaan keempat: {rup14}")
    print("====================================\n")

    total_score2 = score11 + score12 + score13 + score14 
    print(f"Sub Total Nilai Capacity: {total_score2}" + "%")

    print("======================")
    print("\tCondition")
    print("======================\n")

    print("1. Jenis Pekerjaan")
    print("A. Mudah dikerjakan")
    print("B. Masih dapat dikerjakan")
    print("C. Sulit dikerjaka\n")

    jawaban = input("Jawaban Anda: ")
    score15 = 0
    if jawaban == "a":
        score15 = 100 / 100 * 8
    elif jawaban == "b":
        score15 = 66.67 / 100 * 8
    elif jawaban == "c":
        score15 = 33.33 / 100 * 8
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup15 = math.ceil(score15 * 10000)/10000
    print(f"Score untuk pertanyaan pertama: {rup15}")
    print("====================================\n")

    print("2. Periode Kontrak Proyek")
    print("A. < 1 tahun")
    print("B. s/d 1 tahun")
    print("C. > 1 tahun\n")

    jawaban = input("Jawaban Anda: ")
    score16 = 0
    if jawaban == "a":
        score16 = 100 / 100 * 3
    elif jawaban == "b":
        score16 = 66.67 / 100 * 3
    elif jawaban == "c":
        score16 = 33.33 / 100 * 3
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup16 = math.ceil(score16 * 10000)/10000
    print(f"Score untuk pertanyaan kedua: {rup16}")
    print("====================================\n")

    print("3. Lokasi Proyek Terhadap Lokasi Kantor Terjamin")
    print("A. Provinsi yang sama")
    print("B. Provinsi lain")
    print("C. Luar Negeri\n")

    jawaban = input("Jawaban Anda: ")
    score17 = 0
    if jawaban == "a":
        score17 = 100 / 100 * 3
    elif jawaban == "b":
        score17 = 66.67 / 100 * 3
    elif jawaban == "c":
        score17 = 33.33 / 100 * 3
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup17 = math.ceil(score17 * 10000)/10000
    print(f"Score untuk pertanyaan ketiga: {rup17}")
    print("====================================\n")

    print("4. Supply Bahan Baku Proyek")
    print("A. Dari Provinsi sendiri")
    print("B. Dari Provinsi sendiri dan Provinsi lain/luar negeri")
    print("C. Dari Provinsi lain/luar negeri\n")

    jawaban = input("Jawaban Anda: ")
    score18 = 0
    if jawaban == "a":
        score18 = 100 / 100 * 5
    elif jawaban == "b":
        score18 = 66.67 / 100 * 5
    elif jawaban == "c":
        score18 = 33.33 / 100 * 5
    elif jawaban == "exit":
        main()
    else:
        print("Invalid input.")
    rup18 = math.ceil(score18 * 10000)/10000
    print(f"Score untuk pertanyaan keempat: {rup18}")
    print("====================================\n")

    total_score3 = score15 + score16 + score17 + score18
    print(f"Sub Total Nilai Capacity: {total_score3}" + "%")
    total_nilai = total_score + total_score1 + total_score2 + total_score3
    rounded_up = math.ceil(total_nilai * 10000)/10000
    print(f"\nTotal Nilai Bobot: {rounded_up}")
    if 33.33 <= total_nilai <= 59.99:
        print("Keputusan Nilai Bobot: Pengajuan Penerbitan Penjaminan Bank Garansi Ditolak")
    elif 60.00 <= total_nilai <= 77.77:
        print("Keputusan Nilai Bobot: Pengajuan Penerbitan Penjaminan Bank Garansi Diproses dan mengacu ketentuan Agunan Range 2")
    elif 77.78 <= total_nilai <= 100.00:
        print("Keputusan Nilai Bobot: Pengajuan Penerbitan Penjaminan Bank Garansi Diproses dan mengacu ketentuan Agunan Range 1")
    else:
        print("Nilai Invalid.")
        exit()
    print("======================")
    print("Cash Collateral")
    print("======================\n")
    print("Jenis Jaminan: " + jpbg)
    choice_cc = jpbg
    print("SWASTA/BUMN?")
    work_type = str(input("Jawaban anda: "))
    if work_type in ("Swasta", "SWASTA", "swasta"):
        cash_collateral = 0
        if choice_cc in ("Penawaran", "penawaran"):
            print("Tidak ada Agunan")
        elif choice_cc in ("Pelaksanaan", "pelaksanaan"): #Pelaksanaan
            if 33.33 <= total_nilai <= 59.99: #Range 3
                print("Agunan ditolak")
            elif 60.00 <= total_nilai <= 77.77: #Range 2
                if nj <= 500000000:
                    cash_collateral = nj * 0.05
                    print(f"Cash Collateral: Rp.{cash_collateral}")
                elif nj > 500000000:
                    cash_collateral = nj * 0.1
                    print(f"Cash Collateral: Rp.{cash_collateral}")
            elif 77.78 <= total_nilai <= 100: #Range 1
                if nj <= 500000000:
                    print(f"Cash collateral: 0%")
                elif nj > 500000000:
                    cash_collateral = nj * 0.05
                    print(f"Cash collateral: Rp.{cash_collateral}")
        elif choice_cc in ("Uang muka", "uang muka", "Uangmuka", "uangmuka"): #Uang muka
            if 33.33 <= total_nilai <= 59.99: #Range 3
                print("Agunan anda ditolak")
            elif 60.00 <= total_nilai <= 77.77: #Range 2
                if nj <= 500000000:
                    cash_collateral = nj * 0.05
                    print(f"Cash collateral: Rp.{cash_collateral}")
                elif nj > 500000000:
                    cash_collateral = nj * 0.1
                    print(f"Cash collateral: Rp.{cash_collateral}")
            elif 77.78 <= total_nilai <= 100: #Range 1
                if nj <= 500000000:
                    print("Cash collateral: 0%")
                elif nj > 500000000:
                    cash_collateral = nj * 0.05
                    print(f"Cash collateral: Rp.{cash_collateral}")
        elif choice_cc in ("Pemeliharaan", "pemeliharaan"): #Pemeliharaan
            if 33.33 <= total_nilai <= 59.99: #Range 3
                print("Agunan anda ditolak")
            elif 60.00 <= total_nilai <= 77.77: #Range 2
                if nj <= 500000000:
                    cash_collateral = nj * 0.05
                    print(f"Cash collateral: Rp.{cash_collateral}")
                elif nj > 500000000:
                    cash_collateral = nj * 0.1
                    print(f"Cash collateral: Rp.{cash_collateral}")
            elif 77.78 <= total_nilai <= 100: #Range 1
                if nj <= 500000000:
                    print("Cash collateral: 0%")
                elif nj > 500000000:
                    cash_collateral = nj * 0.05
                    print(f"Cash collateral: Rp.{cash_collateral}")
    elif work_type in ("BUMN", "bumn", "Bumn"):
        cash_collateral = 0
        if choice_cc in ("Penawaran", "penawaran"):
            print("Tidak ada Agunan")
        elif choice_cc in ("Pelaksanaan", "pelaksanaan"): #Pelaksanaan
            if 33.33 <= total_nilai <= 59.99: #Range 3
                print("Agunan ditolak")
            elif 60.00 <= total_nilai <= 77.77: #Range 2
                if nj <= 1000000000:
                    cash_collateral = nj * 0.05
                    print(f"Cash Collateral: Rp.{cash_collateral}")
                elif nj > 1000000000:
                    cash_collateral = nj * 0.1
                    print(f"Cash Collateral: Rp.{cash_collateral}")
            elif 77.78 <= total_nilai <= 100: #Range 1
                if nj <= 1000000000:
                    print(f"Cash collateral: 0%")
                elif nj > 1000000000:
                    cash_collateral = nj * 0.05
                    print(f"Cash collateral: Rp.{cash_collateral}")
        elif choice_cc in ("Uang muka", "uang muka", "Uangmuka", "uangmuka"): #Uang muka
            if 33.33 <= total_nilai <= 59.99: #Range 3
                print("Agunan anda ditolak")
            elif 60.00 <= total_nilai <= 77.77: #Range 2
                if nj <= 1000000000:
                    cash_collateral = nj * 0.05
                    print(f"Cash collateral: Rp.{cash_collateral}")
                elif nj > 1000000000:
                    cash_collateral = nj * 0.1
                    print(f"Cash collateral: Rp.{cash_collateral}")
            elif 77.78 <= total_nilai <= 100: #Range 1
                if nj <= 1000000000:
                    print("Cash collateral: 0%")
                elif nj > 1000000000:
                    cash_collateral = nj * 0.05
                    print(f"Cash collateral: Rp.{cash_collateral}")
        elif choice_cc in ("Pemeliharaan", "pemeliharaan"): #Pemeliharaan
            if 33.33 <= total_nilai <= 59.99: #Range 3
                print("Agunan anda ditolak")
            elif 60.00 <= total_nilai <= 77.77: #Range 2
                if nj <= 1000000000:
                    cash_collateral = nj * 0.05
                    print(f"Cash collateral: Rp.{cash_collateral}")
                elif nj > 1000000000:
                    cash_collateral = nj * 0.1
                    print(f"Cash collateral: Rp.{cash_collateral}")
            elif 77.78 <= total_nilai <= 100: #Range 1
                if nj <= 1000000000:
                    print("Cash collateral: 0%")
                elif nj > 1000000000:
                    cash_collateral = nj * 0.05
                    print(f"Cash collateral: Rp.{cash_collateral}")
main()