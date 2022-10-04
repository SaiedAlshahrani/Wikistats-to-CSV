import ssl
import rich
import pandas


# To Override the SSL Error of '[SSL: CERTIFICATE_VERIFY_FAILED]'. 
ssl._create_default_https_context = ssl._create_unverified_context


class Helper:

    def logo_msg():
        rich.print('''
                [dodger_blue2]▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║[/][spring_green4]▌█║▌║│▌║│▌║│▌║│█[/][dodger_blue2]║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌[/]
                [dodger_blue2]▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║[/][red]WIKISTATS-TO-CSV[/][dodger_blue2]║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌[/]
                [dodger_blue2]▌│║▌║▌█║▌║║▌│║▌│║▌║▌█║[/][spring_green4]▌█║▌║│▌║│▌║│▌║│█[/][dodger_blue2]║▌│█║▌│▌║│▌║║▌║▌█║▌║│▌[/]
                ''')


    def get_Wikis_Codes():
        try:
            url = r'https://en.wikipedia.org/wiki/List_of_Wikipedias'
            tables = pandas.read_html(url)
            wikis_codes = tables[3] 
            wikis_codes = wikis_codes[['Wiki', 'Language']]
            wikis_codes = wikis_codes.set_index('Wiki').to_dict()['Language']
            return wikis_codes
        except KeyError:
            wikis_codes = {'en': 'English', 'ceb': 'Cebuano', 'de': 'German', 'sv': 'Swedish', 'fr': 'French', 'nl': 'Dutch', 'ru': 'Russian', 'es': 'Spanish', 'it': 'Italian', 'arz': 'Egyptian Arabic', 'pl': 'Polish', 'ja': 'Japanese', 'zh': 'Mandarin', 'vi': 'Vietnamese', 'war': 'Waray', 'uk': 'Ukrainian', 'ar': 'Arabic', 'pt': 'Portuguese', 'fa': 'Persian', 'ca': 'Catalan', 'sr': 'Serbian', 'id': 'Indonesian', 'ko': 'Korean', 'no': 'Norwegian (Bokmål)', 'fi': 'Finnish', 'tr': 'Turkish', 'hu': 'Hungarian', 'cs': 'Czech', 'ce': 'Chechen', 'sh': 'Serbo-Croatian', 'ro': 'Romanian', 'zh-min-nan': 'Southern Min', 'tt': 'Tatar', 'eu': 'Basque', 'ms': 'Malay', 'eo': 'Esperanto', 'he': 'Hebrew', 'hy': 'Armenian', 'da': 'Danish', 'bg': 'Bulgarian', 'cy': 'Welsh', 'azb': 'South Azerbaijani', 'sk': 'Slovak', 'kk': 'Kazakh', 'et': 'Estonian', 'min': 'Minangkabau', 'be': 'Belarusian', 'simple': 'Simple English', 'el': 'Greek', 'hr': 'Croatian', 'lt': 'Lithuanian', 'gl': 'Galician', 'az': 'Azerbaijani', 'ur': 'Urdu', 'uz': 'Uzbek', 'sl': 'Slovene', 'ka': 'Georgian', 'nn': 'Norwegian (Nynorsk)', 'hi': 'Hindi', 'th': 'Thai', 'ta': 'Tamil', 'la': 'Latin', 'mk': 'Macedonian', 'ast': 'Asturian', 'bn': 'Bengali', 'zh-yue': 'Cantonese', 'lv': 'Latvian', 'tg': 'Tajik', 'af': 'Afrikaans', 'my': 'Burmese', 'mg': 'Malagasy', 'bs': 'Bosnian', 'oc': 'Occitan', 'mr': 'Marathi', 'sq': 'Albanian', 'nds': 'Low German', 'ky': 'Kyrgyz', 'ml': 'Malayalam', 'be-tarask': 'Belarusian (Taraškievica)', 'te': 'Telugu', 'sw': 'Swahili', 'br': 'Breton', 'new': 'Newar', 'jv': 'Javanese', 'lld': 'Ladin', 'vec': 'Venetian', 'ht': 'Haitian Creole', 'pms': 'Piedmontese', 'pnb': 'Western Punjabi', 'su': 'Sundanese', 'lb': 'Luxembourgish', 'ba': 'Bashkir', 'ga': 'Irish', 'ku': 'Kurdish (Kurmanji)', 'lmo': 'Lombard', 'szl': 'Silesian', 'is': 'Icelandic', 'cv': 'Chuvash', 'fy': 'West Frisian', 'ckb': 'Kurdish (Sorani)', 'tl': 'Tagalog', 'wuu': 'Wu', 'an': 'Aragonese', 'sco': 'Scots', 'diq': 'Zazaki', 'pa': 'Punjabi', 'io': 'Ido', 'ne': 'Nepali', 'vo': 'Volapük', 'yo': 'Yoruba', 'gu': 'Gujarati', 'als': 'Alemannic', 'kn': 'Kannada', 'bar': 'Bavarian', 'scn': 'Sicilian', 'ia': 'Interlingua', 'bpy': 'Bishnupriya Manipuri', 'avk': 'Kotava', 'qu': 'Quechua', 'mn': 'Mongolian', 'crh': 'Crimean Tatar', 'nv': 'Navajo', 'xmf': 'Mingrelian', 'ha': 'Hausa', 'si': 'Sinhalese', 'bat-smg': 'Samogitian', 'os': 'Ossetian', 'frr': 'North Frisian', 'ps': 'Pashto', 'ban': 'Balinese', 'or': 'Odia', 'gd': 'Scottish Gaelic', 'cdo': 'Eastern Min', 'yi': 'Yiddish', 'bug': 'Buginese', 'ilo': 'Ilokano', 'sd': 'Sindhi', 'am': 'Amharic', 'sah': 'Sakha', 'nap': 'Neapolitan', 'hsb': 'Upper Sorbian', 'fo': 'Faroese', 'li': 'Limburgish', 'map-bms': 'Banyumasan', 'mai': 'Maithili', 'gor': 'Gorontalo', 'mzn': 'Mazanderani', 'eml': 'Emilian-Romagnol', 'ace': 'Acehnese', 'bcl': 'Central Bikol', 'shn': 'Shan', 'sa': 'Sanskrit', 'zh-classical': 'Classical Chinese', 'wa': 'Walloon', 'ie': 'Interlingue', 'lij': 'Ligurian', 'ig': 'Igbo', 'as': 'Assamese', 'zu': 'Zulu', 'mhr': 'Meadow Mari', 'mrj': 'Hill Mari', 'hyw': 'Western Armenian', 'hif': 'Fiji Hindi', 'mni': 'Meitei', 'km': 'Khmer', 'hak': 'Hakka', 'roa-tara': 'Tarantino', 'pam': 'Kapampangan', 'sn': 'Shona', 'so': 'Somali', 'nso': 'Northern Sotho', 'rue': 'Rusyn', 'bh': 'Bhojpuri', 'se': 'Northern Sami', 'myv': 'Erzya', 'vls': 'West Flemish', 'nds-nl': 'Dutch Low Saxon', 'mi': 'Māori', 'sat': 'Santali', 'sc': 'Sardinian', 'tum': 'Tumbuka', 'nah': 'Nahuatl', 'vep': 'Veps', 'gan': 'Gan', 'tk': 'Turkmen', 'kab': 'Kabyle', 'glk': 'Gilaki', 'fiu-vro': 'Võro', 'co': 'Corsican', 'bo': 'Tibetan', 'ab': 'Abkhazian', 'ary': 'Moroccan Arabic', 'gv': 'Manx', 'frp': 'Franco-Provençal', 'kw': 'Cornish', 'kv': 'Komi', 'pcd': 'Picard', 'csb': 'Kashubian', 'ug': 'Uyghur', 'udm': 'Udmurt', 'skr': 'Saraiki', 'zea': 'Zeelandic', 'ay': 'Aymara', 'gn': 'Guarani', 'mt': 'Maltese', 'nrm': 'Norman', 'bjn': 'Banjar', 'smn': 'Inari Sami', 'lez': 'Lezgian', 'lfn': 'Lingua Franca Nova', 'stq': 'Saterland Frisian', 'lo': 'Lao', 'olo': 'Livvi-Karelian', 'mwl': 'Mirandese', 'rw': 'Kinyarwanda', 'fur': 'Friulian', 'rm': 'Romansh', 'ang': 'Anglo-Saxon', 'lad': 'Ladino', 'gom': 'Konkani', 'koi': 'Komi-Permyak', 'ext': 'Extremaduran', 'tyv': 'Tuvan', 'dsb': 'Lower Sorbian', 'dty': 'Doteli', 'ln': 'Lingala', 'av': 'Avar', 'cbk-zam': 'Chavacano', 'dv': 'Dhivehi', 'ksh': 'Ripuarian', 'pap': 'Papiamento', 'gag': 'Gagauz', 'bxr': 'Buryat', 'pfl': 'Palatinate German', 'pag': 'Pangasinan', 'pi': 'Pali', 'haw': 'Hawaiian', 'awa': 'Awadhi', 'tay': 'Tayal', 'ks': 'Kashmiri', 'tw': 'Twi', 'dag': 'Dagbani', 'inh': 'Ingush', 'mdf': 'Moksha', 'szy': 'Sakizaya', 'krc': 'Karachay-Balkar', 'xal': 'Kalmyk', 'kaa': 'Karakalpak', 'za': 'Zhuang', 'pdc': 'Pennsylvania German', 'atj': 'Atikamekw', 'to': 'Tongan', 'arc': 'Aramaic', 'tcy': 'Tulu', 'kbp': 'Kabiye', 'jam': 'Jamaican Patois', 'na': 'Nauruan', 'wo': 'Wolof', 'kbd': 'Kabardian', 'nia': 'Nias', 'nov': 'Novial', 'tet': 'Tetum', 'ki': 'Kikuyu', 'lg': 'Luganda', 'mnw': 'Mon', 'bi': 'Bislama', 'tpi': 'Tok Pisin', 'nqo': "N'Ko", 'jbo': 'Lojban', 'roa-rup': 'Aromanian', 'fj': 'Fijian', 'lbe': 'Lak', 'kg': 'Kongo', 'xh': 'Xhosa', 'ty': 'Tahitian', 'cu': 'Old Church Slavonic', 'shi': 'Shilha', 'srn': 'Sranan Tongo', 'blk': "Pa'O", 'trv': 'Seediq', 'guw': 'Gungbe', 'om': 'Oromo', 'sm': 'Samoan', 'gcr': 'Guianan Creole', 'alt': 'Altai', 'chr': 'Cherokee', 'ltg': 'Latgalian', 'ny': 'Chewa', 'pih': 'Norfolk', 'got': 'Gothic', 'mad': 'Madurese', 'st': 'Sotho', 'ami': 'Amis', 'tn': 'Tswana', 'bm': 'Bambara', 've': 'Venda', 'rmy': 'Romani', 'ts': 'Tsonga', 'chy': 'Cheyenne', 'rn': 'Kirundi', 'iu': 'Inuktitut', 'ak': 'Akan', 'ss': 'Swazi', 'ff': 'Fula', 'ch': 'Chamorro', 'kcg': 'Tyap', 'pnt': 'Pontic Greek', 'ady': 'Adyghe', 'ik': 'Inupiaq', 'ee': 'Ewe', 'pcm': 'Nigerian Pidgin', 'sg': 'Sango', 'din': 'Dinka', 'pwn': 'Paiwan', 'kl': 'Greenlandic', 'ti': 'Tigrinya', 'dz': 'Dzongkha', 'cr': 'Cree', 'ng': 'Ndonga', 'cho': 'Choctaw', 'kj': 'Kuanyama', 'mh': 'Marshallese', 'ho': 'Hiri Motu', 'ii': 'Nuosu', 'lrc': 'Northern Luri', 'mus': 'Muscogee', 'aa': 'Afar', 'hz': 'Herero', 'kr': 'Kanuri'}
            print(f"\u001b[93mWarning:\u001b[0m Retrieving Wikipedias & its codes was unsuccessful. Unupdated information is provided.")
            print("         To retrieve the latest information, see: https://en.wikipedia.org/wiki/List_of_Wikipedias \n")
            return wikis_codes

    
    def list_Wikis_Codes():
        wikis = Helper.get_Wikis_Codes()
        print(f"## List of `{len(wikis)}` Wikipedias and its languages codes:\n")
        for code, wiki in wikis.items():
            print(f"{wiki}:`{code}`", end=', ')
        print('\n') ; exit()