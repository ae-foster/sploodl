import requests


FORMAT = """http://query.yahooapis.com/v1/public/yql?q=select * from yahoo.finance.xchange where pair in ("%s%s")&format=json&env=store://datatables.org/alltableswithkeys"""
CACHE = {}


def getRate(fromCode, toCode):
    #TODO Could do some caching here
    r = requests.get(FORMAT % (fromCode, toCode))
    return float(r.json()["query"]["results"]["rate"]["Rate"])

def convertValue(amount, fromCode, toCode):
    return amount * getRate(fromCode, toCode)


CURRENCIES = [('GBP', 'GBP'),
    ('EUR', 'EUR'),
    ('USD', 'USD'),
    ('AED', 'AED'),
    ('AFN', 'AFN'),
    ('ALL', 'ALL'),
    ('AMD', 'AMD'),
    ('ANG', 'ANG'),
    ('AOA', 'AOA'),
    ('ARS', 'ARS'),
    ('AUD', 'AUD'),
    ('AWG', 'AWG'),
    ('AZN', 'AZN'),
    ('BAM', 'BAM'),
    ('BBD', 'BBD'),
    ('BDT', 'BDT'),
    ('BGN', 'BGN'),
    ('BHD', 'BHD'),
    ('BIF', 'BIF'),
    ('BMD', 'BMD'),
    ('BND', 'BND'),
    ('BOB', 'BOB'),
    ('BRL', 'BRL'),
    ('BRX', 'BRX'),
    ('BSD', 'BSD'),
    ('BTN', 'BTN'),
    ('BWP', 'BWP'),
    ('BYN', 'BYN'),
    ('BYR', 'BYR'),
    ('BZD', 'BZD'),
    ('CAD', 'CAD'),
    ('CAX', 'CAX'),
    ('CDF', 'CDF'),
    ('CHF', 'CHF'),
    ('CLF', 'CLF'),
    ('CLP', 'CLP'),
    ('CNH', 'CNH'),
    ('CNY', 'CNY'),
    ('COP', 'COP'),
    ('CRC', 'CRC'),
    ('CUC', 'CUC'),
    ('CUP', 'CUP'),
    ('CVE', 'CVE'),
    ('CYP', 'CYP'),
    ('CZK', 'CZK'),
    ('CZX', 'CZX'),
    ('DEM', 'DEM'),
    ('DJF', 'DJF'),
    ('DKK', 'DKK'),
    ('DKX', 'DKX'),
    ('DOP', 'DOP'),
    ('DZD', 'DZD'),
    ('ECS', 'ECS'),
    ('EGP', 'EGP'),
    ('ERN', 'ERN'),
    ('ETB', 'ETB'),
    ('EUR', 'EUR'),
    ('FJD', 'FJD'),
    ('FKP', 'FKP'),
    ('FRF', 'FRF'),
    ('GBP', 'GBP'),
    ('GEL', 'GEL'),
    ('GHS', 'GHS'),
    ('GIP', 'GIP'),
    ('GMD', 'GMD'),
    ('GNF', 'GNF'),
    ('GTQ', 'GTQ'),
    ('GYD', 'GYD'),
    ('HKD', 'HKD'),
    ('HNL', 'HNL'),
    ('HRK', 'HRK'),
    ('HRX', 'HRX'),
    ('HTG', 'HTG'),
    ('HUF', 'HUF'),
    ('HUX', 'HUX'),
    ('IDR', 'IDR'),
    ('IEP', 'IEP'),
    ('ILA', 'ILA'),
    ('ILS', 'ILS'),
    ('INR', 'INR'),
    ('INX', 'INX'),
    ('IQD', 'IQD'),
    ('IRR', 'IRR'),
    ('ISK', 'ISK'),
    ('ISX', 'ISX'),
    ('ITL', 'ITL'),
    ('JMD', 'JMD'),
    ('JOD', 'JOD'),
    ('JPY', 'JPY'),
    ('KES', 'KES'),
    ('KGS', 'KGS'),
    ('KHR', 'KHR'),
    ('KMF', 'KMF'),
    ('KPW', 'KPW'),
    ('KRW', 'KRW'),
    ('KWD', 'KWD'),
    ('KYD', 'KYD'),
    ('KZT', 'KZT'),
    ('LAK', 'LAK'),
    ('LBP', 'LBP'),
    ('LKR', 'LKR'),
    ('LRD', 'LRD'),
    ('LSL', 'LSL'),
    ('LTL', 'LTL'),
    ('LVL', 'LVL'),
    ('LYD', 'LYD'),
    ('MAD', 'MAD'),
    ('MDL', 'MDL'),
    ('MGA', 'MGA'),
    ('MKD', 'MKD'),
    ('MMK', 'MMK'),
    ('MNT', 'MNT'),
    ('MOP', 'MOP'),
    ('MRO', 'MRO'),
    ('MUR', 'MUR'),
    ('MVR', 'MVR'),
    ('MWK', 'MWK'),
    ('MXN', 'MXN'),
    ('MXV', 'MXV'),
    ('MYR', 'MYR'),
    ('MYX', 'MYX'),
    ('MZN', 'MZN'),
    ('NAD', 'NAD'),
    ('NGN', 'NGN'),
    ('NIO', 'NIO'),
    ('NOK', 'NOK'),
    ('NPR', 'NPR'),
    ('NZD', 'NZD'),
    ('OMR', 'OMR'),
    ('PAB', 'PAB'),
    ('PEN', 'PEN'),
    ('PGK', 'PGK'),
    ('PHP', 'PHP'),
    ('PKR', 'PKR'),
    ('PLN', 'PLN'),
    ('PLX', 'PLX'),
    ('PYG', 'PYG'),
    ('QAR', 'QAR'),
    ('RON', 'RON'),
    ('RSD', 'RSD'),
    ('RUB', 'RUB'),
    ('RWF', 'RWF'),
    ('SAR', 'SAR'),
    ('SBD', 'SBD'),
    ('SCR', 'SCR'),
    ('SDG', 'SDG'),
    ('SEK', 'SEK'),
    ('SGD', 'SGD'),
    ('SHP', 'SHP'),
    ('SIT', 'SIT'),
    ('SLL', 'SLL'),
    ('SOS', 'SOS'),
    ('SRD', 'SRD'),
    ('STD', 'STD'),
    ('SVC', 'SVC'),
    ('SYP', 'SYP'),
    ('SZL', 'SZL'),
    ('THB', 'THB'),
    ('TJS', 'TJS'),
    ('TMT', 'TMT'),
    ('TND', 'TND'),
    ('TOP', 'TOP'),
    ('TRY', 'TRY'),
    ('TTD', 'TTD'),
    ('TWD', 'TWD'),
    ('TZS', 'TZS'),
    ('UAH', 'UAH'),
    ('UGX', 'UGX'),
    ('USD', 'USD'),
    ('UYU', 'UYU'),
    ('UZS', 'UZS'),
    ('VEF', 'VEF'),
    ('VND', 'VND'),
    ('VUV', 'VUV'),
    ('WST', 'WST'),
    ('XAF', 'XAF'),
    ('XCD', 'XCD'),
    ('XCU', 'XCU'),
    ('XDR', 'XDR'),
    ('XOF', 'XOF'),
    ('XPF', 'XPF'),
    ('YER', 'YER'),
    ('ZAC', 'ZAC'),
    ('ZAR', 'ZAR'),
    ('ZMW', 'ZMW'),
    ('ZWL', 'ZWL'),
    ]
