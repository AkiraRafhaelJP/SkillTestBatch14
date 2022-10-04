nama, no_peran = '', -1
LIST_PERAN = ['penyihir', 'guard', 'werewolf']

while True:
    nama = input('Masukkan namamu: ')
    if nama == '':
        print('Nama harus diisi!\n')
        continue

    while True:
        print('Terdapat 3 peran: \n1. Penyihir\n2. Guard\n3. Werewolf')
        no_peran = int(input('Masukkan nomor peran yang diinginkan: ').strip())
        if no_peran not in (1, 2, 3):
            print(f'Nomor peran {no_peran} tidak ada. Pilih peranmu untuk memulai game!\n')
            continue
        peran = LIST_PERAN[no_peran-1]
        break
    break

print(f'\nSelamat datang ke game werewolf, {nama} dengan peran {peran}')
