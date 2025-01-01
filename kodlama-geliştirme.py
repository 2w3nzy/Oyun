import sys
import random
import time

print('               ++++++++++++++++++++              ')
print('===========================================')
print('--------Kodlama--Denemesi-----')
print('=============================================')
print('                ++++++++++++++++++++               ')
print('===============================================')
print('                    coded by 2w3nzy                ')
print('===========================================')
print('               ++++++++++++++++++++              ')
print('                                                                               ')             
print('                                                                               ')  
print('                   Sisteme HoşGeldiniz...                       ')
print('                                                                               ')  
print('                                                                               ')  
print('    1  tıklayarak  giriş yapabilirsin.                      ')
print('    2  tıklayarak çıkış yapabilirsin.                       ')      
print('    3  tıklayarak ayarlarına girebilirsiniz            ')  
print('                                                                               ')  
print('                                                                               ')  

option = input('==>: ')

if option == '1':
    print('Sisteme giriş yapıyorsunuz...')
    answer = input('==>: ')
    
    def generate_infinite_binary():
        for _ in range(100): 
            binary_digit = random.choice(['0', '1'])
            print(binary_digit, end='', flush=True)  
            time.sleep(0.1)
        print()  

    generate_infinite_binary()      
           
  
    initial_balance = float(input("Başlangıç bakiyenizi (TL) girin: "))
    balance = initial_balance

    x = 0.00

    while True:
        x_increase = round(random.uniform(0.01, 0.02), 2)  
        x += x_increase
        
        print(f"x değeri: {x}")

        if balance > 0:
            loss_chance = random.random()  
            
            if loss_chance < 0.3:
                loss_amount = round(random.uniform(1, 5), 2)  
                balance -= loss_amount
                print(f"Kayıp: {loss_amount:.2f} TL")

            if x < 10:
                multiplier = random.choice([2, 10])
            elif x < 20:
                multiplier = random.choice([2, 10, 20])
            elif x < 30:
                multiplier = random.choice([2, 10, 20, 30])
            elif x < 50:
                multiplier = random.choice([2, 10, 20, 30, 50])
            else:
                multiplier = random.choice([2, 10, 20, 30, 50, 100])
            
            new_balance = balance * multiplier 
            print(f"Yeni bakiye: {new_balance:.2f} TL")
            balance = new_balance  
            
            continue_choice = input("Devam etmek ister misiniz? (Evet/Hayır): ").strip().lower()
            if continue_choice != '':
                print("Oyun sona erdi.")
                break
        else:
            print("Bakiye bitti.")
            break

        time.sleep(1)  
          
elif option == '2':
    print('Çıkış yapılıyor...')
    sys.exit()
    
elif option == '3':
    print('Ayarlar menüsüne yönlendiriliyorsunuz...')
    
else:
    print('Geçersiz seçenek, lütfen tekrar deneyin.')
    repair = input('0 yap 10 yapma: ')
    
    if repair == '0':
        print('GOOD END')
    elif repair == '10':
        print('kaçma gel BURAYA!!')   
        print('BAD END')    
    else:
        print('Geçersiz giriş.')

time.sleep(1)    
