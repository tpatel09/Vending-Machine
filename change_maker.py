#define variables for money
n = 5
d = 10
q = 25
o = 100
f = 500
quit = True

num_n = 25
num_d = 25
num_q = 25
num_o = 0
num_f = 0

q_give = 0
d_give = 0
n_give = 0

#variables for if change is due from manager
store_f = 0
store_o = 0
store_q = 0
store_d = 0
store_n = 0


#give user information
print("Welcome to the vending machine change maker program")
print("Change maker initialized.")

while quit:
    print("Stock contains:")
    print("  ",num_n, "nickels")
    print("  ",num_d, "dimes")
    print("  ",num_q, "quarters")
    print("  ",num_o, "ones")
    print("  ",num_f, "fives")
    print()


    #get valid input from user
    price = input("Enter the purchase price (xx.xx) or `q' to quit: ")

    if price == 'q':
        quit = False
        total_f = num_f * 5
        total_o = num_o
        total_q = num_q * 0.25
        total_d = num_d * 0.10
        total_n = num_n * 0.05
        total_final = total_f + total_o + total_q + total_d + total_n
        total_dolla = total_final // 1
        total_cen = total_final % 1
        print()
        print("Total:", total_dolla, "dollars and", total_cen, "cents")
        break

    while price.isalpha():
      print("Invalid purchase price. Try again")
      print()
      price = input("Enter the purchase price (xx.xx) or `q' to quit: ")

        
    price = float(price)
    price = round(price*100)
    while price % 5 != 0:
        print("Illegal price: Must be a non-negative mutliple of 5 cents. ")
        print()
        price = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
        price = float(price)
        price = round(price*100)


    #print menu
    print('''
Menu for deposits:
  'n' - deposit a nickel
  'd' - deposit a dime
  'q' - deposit a quarter
  'o' - deposit a one dollar bill
  'f' - deposit a five dollar bill
  'c' - cancel the purchase
    ''')
    

    balance = price
    record = price
    #prompt user for payment
    while balance > 0:
        if balance // 100 != 0:
            dol = balance // 100
            cen = balance % 100
            print("Payment due:", dol, "dollars and", cen, "cents")
        elif balance // 100 == 0:
            cen = balance % 100
            print("Payment due:", cen, "cents")
        deposit = input("Indicate your deposit: ")
        if deposit == 'c':
            print("Please take the change below.")
            print("  No change due.")
            print()
            break
        elif deposit == 'n':
            balance = balance - n
            num_n += 1
        elif deposit == 'd':
            balance = balance - d
            num_d += 1
        elif deposit == 'q':
            balance = balance - q
            num_q += 1
        elif deposit == 'o':
            balance = balance - o
            num_o += 1
        elif deposit == 'f':
            balance = balance - f
            num_f += 1
        elif deposit == 'c':
            print()
            print("Please take the change below.")
            if price >= 25:
                q_give = price // 25
                price = price % 25
                if num_q >= q_give:
                    num_q -= q_give
                    print(' ', q_give, "quarters")
                    q_give = 0
                elif num_q < q_give:
                    q_give -= num_q
                    print(' ', num_q, "quarters")
                    num_q = 0
                if price >= 10:
                    d_give = price // 10
                    price = price % 10
                    if num_d >= d_give:
                        num_d -= d_give
                        print(' ', d_give, "dimes")
                        d_give = 0
                    elif num_d < d_give:
                        d_give -= num_d
                        print(' ', num_d, "dimes")
                        num_d = 0
                    if price >= 5:
                        n_give = price // 5
                        price = price % 5
                        if num_n >= n_give:
                            num_n -= n_give
                            print(' ', n_give, "nickels")
                            n_give = 0
                        elif num_n < n_give:
                            n_give -= num_n
                            print(' ', num_n, "nickels")
                            num_n = 0
                break
            elif price >= 10:
                d_give = price // 10
                price = price % 10
                if num_d >= d_give:
                    num_d -= d_give
                    print(' ', d_give, "dimes")
                    d_give = 0
                elif num_d < d_give:
                    d_give -= num_d
                    print(' ', num_d, "dimes")
                    num_d = 0
                if price >= 5:
                    n_give = price // 5
                    price = price % 5
                    if num_n >= n_give:
                        num_n -= n_give
                        print(' ', n_give, "nickels")
                        n_give = 0
                    elif num_n < n_give:
                        n_give -= num_n
                        print(' ', num_n, "nickels")
                        num_n = 0
                break
            elif price >= 5:
                n_give = price // 5
                price = price % 5
                if num_n >= n_give:
                    num_n -= n_give
                    print(' ', n_give, "nickels")
                    n_give = 0
                elif num_n < n_give:
                    n_give -= num_n
                    print(' ', num_n, "nickels")
                    num_n = 0
                break
        elif deposit != 'n' or deposit != 'd' or deposit != 'q' or deposit != 'o' or deposit != 'f' or deposit != 'c':
            print("Illegal selection:", deposit)
    
    
    if balance == 0:
        print()
        print("Please take the change below.")
        print("  No change due.")
        print()
    elif balance < 0:
        print()
        print("Please take the change below.")
        balance *= -1
        if num_q > 0:
            if balance // 25 > 0:
                q_give = balance // 25
                if num_q >= q_give:
                    num_q -= q_give
                    print(' ', q_give, "quarters")
                    q_give = 0
                    balance = balance % 25
                elif num_q < q_give:
                    q_give_ch = num_q * 25
                    balance -= q_give_ch
                    q_give -= num_q
                    print(' ', num_q, "quarters")
                    num_q = 0
                if balance // 10 > 0:
                    d_give = balance // 10
                    if num_d >= d_give:
                        num_d -= d_give
                        print(' ', d_give, "dimes")
                        d_give = 0
                        balance = balance % 10
                    elif num_d < d_give:
                        d_give_ch = num_d * 10
                        balance -= d_give_ch
                        d_give -= num_d
                        print(' ', num_d, "dimes")
                        num_d = 0
                    if balance // 5 > 0:
                        n_give = balance // 5
                        if num_n >= n_give:
                            num_n -= n_give
                            print(' ', n_give, "nickels")
                            n_give = 0
                            balance = balance % 5
                        elif num_n < n_give:
                            n_give_ch = num_n * 5
                            balance -= n_give_ch
                            n_give -= num_n
                            print(' ', num_n, "nickels")
                            num_n = 0
            if balance // 10 > 0:
                d_give = balance // 10
                if num_d >= d_give:
                    num_d -= d_give
                    print(' ', d_give, "dimes")
                    d_give = 0
                    balance = balance % 10
                elif num_d < d_give:
                    d_give_ch = num_d * 10
                    balance -= d_give_ch
                    d_give -= num_d
                    print(' ', num_d, "dimes")
                    num_d = 0
                if balance // 5 > 0:
                    n_give = balance // 5
                    if num_n >= n_give:
                        num_n -= n_give
                        print(' ', n_give, "nickels")
                        n_give = 0
                        balance = balance % 5
                    elif num_n < n_give:
                        n_give_ch = num_n * 5
                        balance -= n_give_ch
                        n_give -= num_n
                        print(' ', num_n, "nickels")
                        num_n = 0
            if balance // 5 > 0:
                n_give = balance // 5
                if num_n >= n_give:
                    num_n -= n_give
                    print(' ', n_give, "nickels")
                    n_give = 0
                    balance = balance % 5
                elif num_n < n_give:
                    n_give_ch = num_n * 5
                    balance -= n_give_ch
                    n_give -= num_n
                    print(' ', num_n, "nickels")
                    num_n = 0
    



    #change due if out of change
    #give_tot = q_give + d_give + n_give
    #if balance > 0:
    #    if give_tot // 500 != 0:
    #        store_f = give_tot // 500
    #        give_tot = give_tot % 500
    #        if give_tot // 100 != 0:
    #            store_o = give_tot // 100
    #            give_tot = give_tot % 100
    #            if give_tot // 25 != 0:
    #                store_q = give_tot // 25
    #                give_tot = give_tot % 25
    #                if give_tot // 10 != 0:
    #                    store_d = give_tot // 10
    #                    give_tot = give_tot % 10
    #                    if give_tot // 5 != 0:
    #                        store_n = give_tot // 5
    #    elif give_tot // 100 != 0:
    #        store_o = give_tot // 100
    #        give_tot = give_tot % 100
    #        if give_tot // 25 != 0:
    #            store_q = give_tot // 25
    #            give_tot = give_tot % 25
    #            if give_tot // 10 != 0:
    #                store_d = give_tot // 10
    #                give_tot = give_tot % 10
    #                if give_tot // 5 != 0:
    #                    store_n = give_tot // 5
    #    elif give_tot // 25 != 0:
    #        store_q = give_tot // 25
    #        give_tot = give_tot % 25
    #        if give_tot // 10 != 0:
    #            store_d = give_tot // 10
    #            give_tot = give_tot % 10
    #            if give_tot // 5 != 0:
    #                store_n = give_tot // 5
    #    elif give_tot // 10 != 0:
    #        store_d = give_tot // 10
    #        give_tot = give_tot % 10
    #        if give_tot // 5 != 0:
    #            store_n = give_tot // 5
    #    elif give_tot // 5 != 0:
    #        store_n = give_tot // 5
    #    amt_due_dolla = store_f + store_o
    #    amt_due_cent = store_q + store_d + store_n           
    #    
    #    if amt_due_dolla > 0:
    #        print("Machine is out of change.")
    #        print("See store manager for remaining refund.")
    #        print("Amount due is:", amt_due_dolla, "dollars and", amt_due_cent, "cents")
    #    elif amt_due_cent > 0 and amt_due_dolla == 0:
    #        print("Machine is out of change.")
    #        print("See store manager for remaining refund.")
    #        print("Amount due is:", amt_due_cent, "cents")
