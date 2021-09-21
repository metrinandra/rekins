import aprekins


def print_info():
    # Programmu palaižot,
    # uz ekrāna tiek izvadīts īss apraksts par programmas darbību.
    print('Programma rekina sagatavosanai')


def lietotaja_ievade():
    # User input:
    # klienta vārdu (simbolu virkni);
    # veltījuma tekstu (simbolu virkni);
    # lādītes izmēru – platumu, garumu un augstumu milimetros (veselus skaitļus);
    # kokmateriāla cenu EUR/m 2 .
    vards = input('Ieraksti vardu: ')
    veltijuma_teksts = input('Ievadi veltijuma tekstu kastitei: ')
    platums = input('Cik plata kastite? ***Noraadi milimetrus. Tikai veseli skaitli!***')
    garums = input('Cik  plata garumaa? ***Noraadi milimetrus.Tikai veseli skaitli!***')
    augstums = input('Cik  augsta? ***Noraadi milimetrus.Tikai veseli skaitli!***')
    izmeri = [platums, augstums, garums]
    kokmateriala_cena = input('Kokmateriala cena')
    rekins = aprekins.Aprekins(vards, veltijuma_teksts, izmeri, kokmateriala_cena)
    aprekins.Aprekins.aprekinat_laukumu(rekins)


# Programmas rekins main()
if __name__ == '__main__':
    print_info()
    while True:
        lietotaja_ievade()
        run_again = input('Vai velies sagatavot rekinu velreiz? JAA - 1, NEE - 0')
        if run_again == 1:
            continue
        else:
            exit(0)
