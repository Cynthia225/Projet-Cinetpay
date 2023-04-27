import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as nb

# Importer les fichiers excel
Payin = pd.read_excel(r'C:\Users\nanih\Downloads\PayIn.xlsx')
Payout = pd.read_excel(r'C:\Users\nanih\Downloads\PayOut.xlsx')
Airtime = pd.read_excel(r'C:\Users\nanih\Downloads\Airtime (1).xlsx')
Produits = pd.concat([Payin, Payout, Airtime]) #concatener les 3 fichiers excel PayIn, PayOut et Airtime
print(Produits.head())

def AllProduits():
# La fonction AllProduits affiche pour chaque opérateur les produits les plus utilisées

    prdts = Produits.groupby('produit')
    f_payin = prdts.get_group('Payin')['produit'].value_counts()
    f_payout = prdts.get_group('Payout')['produit'].value_counts()
    f_rtime = prdts.get_group('Airtime')['produit'].value_counts()
    ordonne = prdts['operateur'].value_counts().index
    services = prdts['produit'].value_counts().index
    pos = nb.arange(len(ordonne))
    plt.barh(pos, f_payin, color='lightsteelblue')
    plt.barh(pos, f_payout, color='IndianRed')
    plt.barh(pos, f_rtime, color='green')
    plt.yticks(pos, ordonne)
    plt.ylabel('operateur')
    plt.title('Montant par Opérateur et par Produits', fontsize=6)
    plt.legend(services, loc=1)
    plt.show()

AllProduits()

