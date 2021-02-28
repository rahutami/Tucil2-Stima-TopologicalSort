import course_13519192 as course
import topologicalsort_13519192 as ts
import util_13519192 as u

# Meminta path ke file yang ingin dibuka
fileName = input("Masukkan path ke file daftar mata kuliah: ")

# Mengambil data dari file tersebut
courseList = u.getCoursesData(fileName)

# Mencari rencana studi yang mungkin diambil oleh mahasiswa
# Memanggil topological sort
coursesPlan = ts.topologicalSort(courseList)

# Mencetak hasil topological sort
u.printResult(coursesPlan)