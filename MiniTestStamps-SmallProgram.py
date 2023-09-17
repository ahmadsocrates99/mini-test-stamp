a = range(1, 101)                       # untuk membuat urutan angka 1 s/d 100, kenapa harus 1 dan 101 di (1, 101) karena default awal selalu 0 maka di tulis 1 dan 101
m = []                                  # untuk menampung hasil penseleksian

for n in reversed(a):                   # melooping value yang berada di variable a dan revresed untuk membalik value yang berada di variable a
    v = []                              # variable penampung hasil pembagian lebih dari 2 pembagian untuk mencari bilangan prima
    for k in a:                         # melooping value untuk pembagiannya
        if int(n % k) == 0:             # menseleksi sisa bagi 0 untuk mencari bilangan prima
            v.append(0)                 # menambahkan sisa bagi 0 ke variable penampung 
    if len(v) != 2:                     # hanya menampilkan bilangan yang bisa di bagi lebih dari 2 bilangan atau bilangan bukan prima
        if ((n % 5) + (n % 3)) == 0:    # mencari value yang bisa di bagi 5 dan di bagi 3
            m.append("FooBar")
        elif n % 3 == 0:                # mencari value yang bisa di bagi 3
            m.append("Foo")
        elif n % 5 == 0:                # mencari value yang bisa di bagi 3
            m.append("Bar")
        else:                           # nilai yang tidak bisa di bagi 5 dan 3, 5, 3
            m.append(str(n))            

print(', '.join(m))                     # untuk menggabungkan value di list dan di batasi setiap value[index] dengan ', '
        