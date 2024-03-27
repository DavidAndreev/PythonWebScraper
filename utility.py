def dokumentyToString(documents):
    """Turns list of documents into a single string with each document in one line"""
    finalString = ''
    for doc in documents:
        finalString = f'{finalString}Druh: {doc['druhDokumentu']} Názov: {
            doc['nazovDokumentu']} Zverejnenie: {doc['zverejnenie']}  Uprava: {doc['uprava']} \n'
    return finalString


def oznameniaToString(oznamenia):
    """Turns list of oznamenia into a single string with each oznamenie in one line"""
    finalString = ''
    for doc in oznamenia:
        finalString = f'{finalString}Skratka: {doc['skratka']} Dátum zverejnenia: {
            doc['datumZverejnenia']} URL oznámenia: {doc['urlOznamenie']} \n'
    return finalString
