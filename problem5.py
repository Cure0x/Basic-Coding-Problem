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

def merge_unique(array1, array2):
    merged = array1.copy()
    for value in array2:
        if value not in merged:
            merged.append(value)
    return merged

def finding_Route (route, start, finish):
    answers, dists = [],[]
    node = start
    distance = 0
    next_Nodes = list(route[node].keys())
    stack = [next_Nodes]
    path = [node]
    
    while len(stack) != 0 :
        if node == finish:
            answers.append(path)
            dists.append(distance)
            pass
        else:
            next_Nodes = list(route[node].keys())
            stack = merge_unique(stack, next_Nodes)
            next_Path = stack[-1]
            distance += route[node][next_Path]
            node = next_Path
            path.append(node)
    return answers, dists

answers , dists = finding_Route(graph_Jarak, 'A', 'E')

for i in range(len(answers)):
    print (f'''Path {i} = {answers[i]} dengan jarak {dists[i]}''')