def topologicalSort(courses):
    # Apabila sudah tidak ada course yang perlu diambil lagi kembalikan list kosong
    if(len(courses) == 0):
        return []
    else:
        courseThisSemester = []
        i = 0
        while (i < len(courses)):
            # Mengecek apakah suatu mata kuliah memiliki prereqs atau tidak
            if(len(courses[i].prereqs) == 0):
                # Jika tidak memiliki prereqs, ambil mata kuliah tersebut dan hapus dari daftar mata kuliah
                courseThisSemester.append(courses[i].courseID)
                courses.remove(courses[i])
            else:
                # Jika memiliki prereqs lanjutkan pencarian
                i += 1
        
        # Menghapus mata kuliah yang telah diambil dari prereqs mata kuliah-mata kuliah yang belum diambil
        for course in courses:
            for takenCourse in courseThisSemester:
                if course.hasPrereq(takenCourse):
                    course.prereqs.remove(takenCourse)

        # Panggil topologicalsort dengan argumen list berisi mata kuliah-kuliah yang belum diambil
        # Simpan di list nextSemestersCourses
        nextSemestersCourses = topologicalSort(courses)

        # Apabila nextSemesterCourses adalah list kosong, berarti mata kuliah yang diambil pada pencarian ini adalah mata kuliah yang diambil pada semester "terakhir"
        # Kembalikan list of list yang berisi daftar mata kuliah yang dipilih pada pencarian ini
        if(nextSemestersCourses == []):
            return [courseThisSemester]

        # Jika nextSemestersCourses bukan list kosong, berarti mata kuliah yang diambil pada pencarian ini bukan mata kuliah yang diambil pada semester "terakhir"
        # Masukkan list courseThisSemester di index ke-0 nextSemestersCourses
        nextSemestersCourses.insert(0, courseThisSemester)

        # Kembalikan nextSemestersCourses
        return nextSemestersCourses