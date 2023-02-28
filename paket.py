from pkg.modul1 import *
from pkg.modul2 import *
from pkg.hitungnilai import hitung_nilai
from pkg.hitungnilai import nilai_tambahan

def main():
    #memanggil fungsi fungsi dalam modul
    f1()
    f2()
    #memanggil fungsi fungsi dalam modul
    f3()
    f4()
    print("Nilai Akhir: ",hitung_nilai(75,97))
    print("Nilai tambahan : ", hitung_nilai(50,80))
main()