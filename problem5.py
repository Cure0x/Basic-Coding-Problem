graph_Jarak ={
    "A": {
        "B":7,
        "C":9,
        "F":14
    },

    "B": {
        "A":7,
        "C":10,
        "D":10
    },

    "C": {
        "A":9,
        "B":10,
        "D":11,
        "F":2
    },

    "D": {
        "B":15,
        "C":11,
        "E":6
    },

    "E": {
        "D":6,
        "F":9
    },

    "F": {
        "A":14,
        "C":2,
        "E":9
    }
}

# Define start dan akhir
# Dari start, cek node apa aja selanjutnya
# Cek salah satu node lalu cek node selanjutnya
# Setiap pengecekan tidak boleh kembali ke node yang pernah dijalani
# Cek apakah sudah bertemu node akhir atau belum
# Jika belum bertemu coba lagi
# Jika sudah bertemu dengan Node E, simpan semua node yang dilalui dan jumlah weight yang dilewati oleh perjalanan pencarian jalan tersebut ke dalam list (?)
# Selanjutnya coba di percabangan sebelumnya yang belum dicek

#Karena dalam pencarian jalan kita akan mencari dan melakukan decisiion di yang paling akhir maka menggunakan data structure stack
# Karena tidak boleh melewati jalan yang sama, maka stack akan menggunakan set

def finding_Route (route, start, finish):
    stack = []
    distance = 0
    node = start
    if node != finish:
        path = [node]
        next_Nodes = list(route[node].keys())
        print(f"path before update = {path}")
        print(f"next node = {next_Nodes}")
        stack += next_Nodes
        next_Path = stack[-1]
        distance = route[node][next_Path]
        node = next_Path
        path.append(node)
        print(f"path after update = {path}")
        print(f"Total Distance = {distance}")
        print(f"All the stack after update = {stack}")
        print(f"The node that we are now = {node}")

    pass

finding_Route(graph_Jarak, 'A', 'E')