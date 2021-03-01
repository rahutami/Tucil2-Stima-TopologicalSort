import course_13519192 as course
import topologicalsort_13519192 as ts
import util_13519192 as u

# Meminta path ke file yang ingin dibuka
inputFile = input("Masukkan path ke file daftar mata kuliah: ")
print()

# Mengambil data dari file tersebut
courseList = u.getCoursesData(inputFile)

# Mencari rencana studi yang mungkin diambil oleh mahasiswa
# Memanggil topological sort
coursesPlan = ts.topologicalSort(courseList)

# Mencetak hasil topological sort
u.printResult(coursesPlan)

saveOutputInFile = input("Apakah Anda ingin menyimpan rencana studi di dalam sebuah file? Ya/Tidak: ")
print()

if(saveOutputInFile == "Ya"):
    outputFile = input("Masukkan path ke file penyimpanan (format .txt): ")
    print()
    u.saveResult(outputFile, coursesPlan, inputFile)
