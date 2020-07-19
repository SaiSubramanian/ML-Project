import CntryToGeo as ctg
import pandas as pd

params = []
sector = ['SECTOR_Communications Sector', 'SECTOR_Computer Service Industry Sector', 'SECTOR_Distribution Sector',
          'SECTOR_Enterprise', 'SECTOR_Financial Services Sector', 'SECTOR_Industrial Sector', 'SECTOR_Mid market',
          'SECTOR_Public Sector', 'SECTOR_Unassigned Sector', 'SECTOR_Unknown']
Cgeo = []
for g in list(ctg.contractGeo.keys()):
    Cgeo.append('CONTRACT_GEO_' + str(g))

rqstType = ['REQUEST TYPE_Catalog only', 'REQUEST TYPE_Catalog Request Change',
            'REQUEST TYPE_Predefined Solution Request', 'REQUEST TYPE_Project Change Request',
            'REQUEST TYPE_Request For Service (RFS)', 'REQUEST TYPE_Unknown']

cmplxty = ['COMPLEXITY_Catalog Request Change', 'COMPLEXITY_Complex', 'COMPLEXITY_Ctlg Only', 'COMPLEXITY_Medium',
           'COMPLEXITY_PDS', 'COMPLEXITY_Project Change Request', 'COMPLEXITY_Simple', 'COMPLEXITY_Unknown']

prpsl = ['PROPOSAL_PRICING_TERM_Firm (Best and Final)', 'PROPOSAL_PRICING_TERM_Non-binding',
         'PROPOSAL_PRICING_TERM_Unknown']

txn = ['TXN_TYPE_DESC_Contract Renewal/Renegotiation/Extension', 'TXN_TYPE_DESC_RFP/RFQ',
       'TXN_TYPE_DESC_RFS/Predefined/Catalog only', 'TXN_TYPE_DESC_RU/ARC/RRC transaction only',
       'TXN_TYPE_DESC_Unknown']


def getParams():
    params.extend(Cgeo)
    params.extend(rqstType)
    params.extend(cmplxty)
    params.extend(prpsl)
    params.extend(sector)
    params.extend(txn)
    return params
    # return list with all values
