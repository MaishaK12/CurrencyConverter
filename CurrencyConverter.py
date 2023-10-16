#declare all variables
done = False

#Canadian dollar conversions 
cad_usd = 1.0220 
cad_euro = 0.7935 
cad_gbp = 0.6387 
cad_jpy = 79.9794 
cad_cny = 6.4295 
cad_chf = 0.9614 
cad_inr = 53.8968 

#US dollar conversions  
usd_cad = 0.9785 
usd_euro = 0.7764 
usd_gbp = 0.6250 
usd_jpy = 78.2584 
usd_cny = 6.2895 
usd_chf = 0.9407 
usd_inr = 52.7345 

#European euro conversions  
euro_cad = 1.2602 
euro_usd = 1.2879 
euro_gbp = 0.8049 
euro_jpy = 100.7700 
euro_cny = 8.0987 
euro_chf = 1.2113 
euro_inr = 67.9060 

#UK pound conversions  
gbp_cad = 1.5656 
gbp_usd = 1.6000 
gbp_euro = 1.2425 
gbp_jpy = 125.2000 
gbp_cny = 10.0611 
gbp_chf = 1.5052 
gbp_inr = 84.3593 

#Japanese yen coversions  
jpy_cad = 0.1250 
jpy_usd = 0.1278 
jpy_euro = 0.0099 
jpy_gbp = 0.0080 
jpy_cny = 0.0804 
jpy_chf = 0.0120 
jpy_inr = 0.6739 

#Chinese yuan conversions  
cny_cad = 0.1555 
cny_usd = 0.1590 
cny_euro = 0.1235 
cny_gbp = 0.0994 
cny_jpy = 12.4425 
cny_chf = 0.1496 
cny_inr = 8.3847 

#Switzerland franc conversions  
chf_cad = 1.0402 
chf_usd = 1.0630 
chf_euro = 0.8255 
chf_gbp = 0.6644 
chf_jpy = 83.1635 
chf_cny = 6.6838 
chf_inr = 56.0441 

#Indian rupee conversions  
inr_cad = 0.1855 
inr_usd = 0.0190 
inr_euro = 0.0147 
inr_gbp = 0.0119 
inr_jpy = 1.4839 
inr_cny = 0.1193 
inr_chf = 0.0178 


#retrieve Info 
currency = (input("Please enter currency in hand:"))    
currency_required = (input("Please enter currency required:"))    
amount = int (input("Please enter amount (currency value):"))


#calculate
while not done: 
	#for cad 
    if currency == "cad": 
        if currency_required == "usd": 
            cad_to_usd = amount * cad_usd 
            print(amount, "in", currency_required, "is equivalent to", (format(cad_to_usd, '.2f'))) 
        if currency_required == "euro": 
            cad_to_euro = amount * cad_euro 
            print(amount, "in", currency_required, "is equivalent to", (format(cad_to_euro, '.2f')))
        if currency_required == "gbp": 
            cad_to_gbp = amount * cad_gbp 
            print(amount, "in", currency_required, "is equivalent to", (format(cad_to_gbp, '.2f')))
        if currency_required == "jpy": 
            cad_to_jpy = amount * cad_jpy 
            print(amount, "in", currency_required, "is equivalent to", (format(cad_to_jpy, '.2f')))
        if currency_required == "cny": 
            cad_to_cny = amount * cad_cny 
            print(amount, "in", currency_required, "is equivalent to", (format(cad_to_cny, '.2f')))
        if currency_required == "chf": 
            cad_to_chf = amount * cad_chf 
            print(amount, "in", currency_required, "is equivalent to", (format(cad_to_chf, '.2f')))
        if currency_required == "inr": 
            cad_to_inr = amount * cad_inr
            print(amount, "in", currency_required, "is equivalent to", (format(cad_to_inr, '.2f')))
    
    #for usd 
    elif currency == "usd": 
        if currency_required == "cad": 
            usd_to_cad = amount * usd_cad 
            print(amount, "in", currency_required, "is equivalent to", (format(usd_to_cad, '.2f')))
        if currency_required == "euro": 
            usd_to_euro = amount * usd_euro 
            print(amount, "in", currency_required, "is equivalent to", (format(usd_to_euro, '.2f')))
        if currency_required == "gbp": 
            usd_to_gbp = amount * usd_gbp 
            print(amount, "in", currency_required, "is equivalent to", (format(usd_to_gbp, '.2f')))
        if currency_required == "jpy": 
            usd_to_jpy = amount * usd_jpy 
            print(amount, "in", currency_required, "is equivalent to", (format(usd_to_jpy, '.2f')))
        if currency_required == "cny": 
            usd_to_cny = amount * usd_cny 
            print(amount, "in", currency_required, "is equivalent to", (format(usd_to_cny, '.2f')))
        if currency_required == "chf": 
            usd_to_chf = amount * usd_chf 
            print(amount, "in", currency_required, "is equivalent to", (format(usd_to_chf, '.2f')))
        if currency_required == "inr": 
            usd_to_inr = amount * usd_inr 
            print(amount, "in", currency_required, "is equivalent to", (format(usd_to_inr, '.2f')))

    #for euro 
    elif currency == "euro": 
        if currency_required == "cad": 
            euro_to_cad = amount * euro_cad 
            print(amount, "in", currency_required, "is equivalent to", (format(euro_to_cad, '.2f')))
        if currency_required == "usd": 
            euro_to_usd = amount * euro_usd 
            print(amount, "in", currency_required, "is equivalent to", (format(euro_to_usd, '.2f')))
        if currency_required == "gbp": 
            euro_to_gbp = amount * euro_gbp 
            print(amount, "in", currency_required, "is equivalent to", (format(euro_to_gbp, '.2f')))
        if currency_required == "jpy": 
            euro_to_jpy = amount * euro_jpy 
            print(amount, "in", currency_required, "is equivalent to", (format(euro_to_jpy, '.2f')))
        if currency_required == "cny": 
            euro_to_cny = amount * euro_cny 
            print(amount, "in", currency_required, "is equivalent to", (format(euro_to_cny, '.2f')))
        if currency_required == "chf": 
            euro_to_chf = amount * euro_chf 
            print(amount, "in", currency_required, "is equivalent to", (format(euro_to_chf, '.2f')))
        if currency_required == "inr": 
            euro_to_inr = amount * euro_inr 
            print(amount, "in", currency_required, "is equivalent to", (format(euro_to_inr, '.2f')))

    #for gbp 
    elif currency == "gbp": 
        if currency_required == "cad": 
            gbp_to_cad = amount * gbp_cad 
            print(amount, "in", currency_required, "is equivalent to", (format(gbp_to_cad, '.2f')))
        if currency_required == "usd": 
            gbp_to_usd = amount * gbp_usd 
            print(amount, "in", currency_required, "is equivalent to", (format(gbp_to_usd, '.2f')))
        if currency_required == "euro": 
            gbp_to_euro = amount * gbp_euro 
            print(amount, "in", currency_required, "is equivalent to", (format(gbp_to_euro, '.2f')))
        if currency_required == "jpy": 
            gbp_to_jpy = amount * gbp_jpy 
            print(amount, "in", currency_required, "is equivalent to", (format(gbp_to_jpy, '.2f')))
        if currency_required == "cny": 
            gbp_to_cny = amount * gbp_cny 
            print(amount, "in", currency_required, "is equivalent to", (format(gbp_to_cny, '.2f')))
        if currency_required == "chf": 
            gbp_to_chf = amount * gbp_chf 
            print(amount, "in", currency_required, "is equivalent to", (format(gbp_to_chf, '.2f')))
        if currency_required == "inr": 
            gbp_to_inr = amount * gbp_inr 
            print(amount, "in", currency_required, "is equivalent to", (format(gbp_to_inr, '.2f')))

    #for jpy 
    elif currency == "jpy": 
        if currency_required == "cad": 
            jpy_to_cad = amount * jpy_cad 
            print(amount, "in", currency_required, "is equivalent to", (format(jpy_to_cad, '.2f')))
        if currency_required == "usd": 
            jpy_to_usd = amount * jpy_usd 
            print(amount, "in", currency_required, "is equivalent to", (format(jpy_to_usd, '.2f')))
        if currency_required == "euro": 
            jpy_to_euro = amount * jpy_euro 
            print(amount, "in", currency_required, "is equivalent to", (format(jpy_to_euro, '.2f')))
        if currency_required == "gbp": 
            jpy_to_gbp = amount * jpy_gbp 
            print(amount, "in", currency_required, "is equivalent to", (format(jpy_to_gbp, '.2f')))
        if currency_required == "cny": 
            jpy_to_cny = amount * jpy_cny 
            print(amount, "in", currency_required, "is equivalent to", (format(jpy_to_cny, '.2f')))
        if currency_required == "chf": 
            jpy_to_chf = amount * jpy_chf 
            print(amount, "in", currency_required, "is equivalent to", (format(jpy_to_chf, '.2f')))
        if currency_required == "inr": 
            jpy_to_inr = amount * jpy_inr 
            print(amount, "in", currency_required, "is equivalent to", (format(jpy_to_inr, '.2f')))

    #for cny 
    elif currency == "cny": 
        if currency_required == "cad": 
            cny_to_cad = amount * cny_cad 
            print(amount, "in", currency_required, "is equivalent to", (format(cny_to_cad, '.2f')))
        if currency_required == "usd": 
            cny_to_usd = amount * cny_usd 
            print(amount, "in", currency_required, "is equivalent to", (format(cny_to_usd, '.2f')))
        if currency_required == "euro": 
            cny_to_euro = amount * cny_euro 
            print(amount, "in", currency_required, "is equivalent to", (format(cny_to_euro, '.2f')))
        if currency_required == "gbp": 
            cny_to_gbp = amount * cny_gbp 
            print(amount, "in", currency_required, "is equivalent to", (format(cny_to_gbp, '.2f')))
        if currency_required == "jpy": 
            cny_to_jpy = amount * cny_jpy 
            print(amount, "in", currency_required, "is equivalent to", (format(cny_to_jpy, '.2f')))
        if currency_required == "chf": 
            cny_to_chf = amount * cny_chf 
            print(amount, "in", currency_required, "is equivalent to", (format(cny_to_chf, '.2f')))
        if currency_required == "inr": 
            cny_to_inr = amount * cny_inr 
            print(amount, "in", currency_required, "is equivalent to", (format(cny_to_inr, '.2f')))

    #for chf 
    elif currency == "chf": 
        if currency_required == "cad": 
            chf_to_cad = amount * chf_cad 
            print(amount, "in", currency_required, "is equivalent to", (format(chf_to_cad, '.2f')))
        if currency_required == "usd": 
            chf_to_usd = amount * chf_usd 
            print(amount, "in", currency_required, "is equivalent to", (format(chf_usd, '.2f')))
        if currency_required == "euro": 
            chf_to_euro = amount * chf_euro 
            print(amount, "in", currency_required, "is equivalent to", (format(chf_euro, '.2f')))
        if currency_required == "gbp": 
            chf_to_gbp = amount * chf_gbp 
            print(amount, "in", currency_required, "is equivalent to", (format(chf_gbp, '.2f')))
        if currency_required == "jpy": 
            chf_to_jpy = amount * chf_jpy 
            print(amount, "in", currency_required, "is equivalent to", (format(chf_jpy, '.2f')))
        if currency_required == "cny": 
            chf_to_cny = amount * chf_cny 
            print(amount, "in", currency_required, "is equivalent to", (format(chf_cny, '.2f')))
        if currency_required == "inr": 
            chf_to_inr = amount * chf_inr 
            print(amount, "in", currency_required, "is equivalent to", (format(chf_inr, '.2f')))

    #for inr 
    elif currency == "inr": 
        if currency_required == "cad": 
            inr_to_cad = amount * inr_cad 
            print(amount, "in", currency_required, "is equivalent to", (format(inr_to_cad, '.2f')))
        if currency_required == "usd": 
            inr_to_usd = amount * inr_usd 
            print(amount, "in", currency_required, "is equivalent to", (format(inr_to_usd, '.2f')))
        if currency_required == "euro": 
            inr_to_euro = amount * inr_euro 
            print(amount, "in", currency_required, "is equivalent to", (format(inr_to_euro, '.2f')))
        if currency_required == "gbp": 
            inr_to_gbp = amount * inr_gbp 
            print(amount, "in", currency_required, "is equivalent to", (format(inr_to_gbp, '.2f')))
        if currency_required == "jpy": 
            inr_to_jpy = amount * inr_jpy 
            print(amount, "in", currency_required, "is equivalent to", (format(inr_to_jpy, '.2f')))
        if currency_required == "cny": 
            inr_to_cny = amount * inr_cny 
            print(amount, "in", currency_required, "is equivalent to", (format(inr_to_cny, '.2f')))
        if currency_required == "chf": 
            inr_to_chf = amount * inr_chf 
            print(amount, "in", currency_required, "is equivalent to", (format(inr_to_chf, '.2f')))
        
        keep_going = (input("Do you want to keep converting? Enter Y to continue and N to stop:")).upper() 
    if keep_going == "Y":
        done = False
        currency = (input("Please enter currency in hand:"))    
        currency_required = (input("Please enter currency required:"))    
        amount = int (input("Please enter amount (currency value):"))
    if keep_going == "N":
        done = True
        print("Conversion has ended.")    