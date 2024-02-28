import requests
import pandas as pd

def summarize_state_res(state):
    url = f"https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/{state}/{state}-c0001-e000544-r.json"
    j = requests.get(url).json()
    
    other_votes = pd.Series(
    {
        'abstencoes': j['a'],
        'brancos': j['vb'],
        'nulos': j['vn']
    }
    )
    candidates = pd.DataFrame(j['cand']).set_index("nm")['vap']
    return pd.concat([candidates, other_votes])


def summarize_state_res_2nd(state):
    url = f"https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/{state}/{state}-c0001-e000545-r.json"
    j = requests.get(url).json()
    
    other_votes = pd.Series(
    {
        'abstencoes': j['a'],
        'brancos': j['vb'],
        'nulos': j['vn']
    }
    )
    candidates = pd.DataFrame(j['cand']).set_index("nm")['vap']
    return pd.concat([candidates, other_votes])