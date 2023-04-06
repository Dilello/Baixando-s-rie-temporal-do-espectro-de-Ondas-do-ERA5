#================================================================================================
# Título: Donwload do spectro horário de ondas gerados por modelo determinístico do ERA5
# Fonte: Baseado em códigos fornecidos no site do ERA5
# Autor: Marcelo Di Lello Jordão
# Contato: dilellocn@gmail.com
# Objetivo: gerar arquivos diários com extensão .nc onde estarão armazenados espectros 
# horários de onda com 24 direções e 30 frequências dentro de um recorte geográfica de interesse. 
#=================================================================================================

# BIBLIOTECAS
import pandas as pd
import numpy as np
import cdsapi

# RECORTE GEOGRÁFICO
# latitude e longitude me grau decimal
lonEast=-36
lonWest=-41
latSouth=-22
latNorth=-16

# PERÍODO DE INTERESSE
datas = pd.date_range('2022-8-1','2022-8-31').astype(str)
mes = 'ago'
ano = '2022'

# DOWNLOAD DOS DADOS
for i in np.arange(0,len(datas)):
    c = cdsapi.Client()
    c.retrieve(
    'reanalysis-era5-complete',{
    'class': 'ea',
    'date': datas[i],
    'direction': '1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24',
    'domain': 'g',
    'expver': '1',
    'frequency': '1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30',
    'param': '251.140',
    'stream': 'wave',
    'time': '00:00:00/01:00:00/02:00:00/03:00:00/04:00:00/05:00:00/06:00:00/07:00:00/08:00:00/09:00:00/10:00:00/11:00:00/12:00:00/13:00:00/14:00:00/15:00:00/16:00:00/17:00:00/18:00:00/19:00:00/20:00:00/21:00:00/22:00:00/23:00:00',
    'area': str(latNorth) + '/' + str(lonWest) + '/' + str(latSouth) + '/' + str(lonEast), # Norte, Oeste, Sul, Leste. Default: global
    'grid': '0.5/0.5', # Latitude/longitude. Default: spherical harmonics or reduced Gaussian grid
    'type': 'an',
    'format': 'netcdf', 
    },  'ERA5_DetSpec_'+str(i+1)+mes+ano+'.nc') # Arquivo será salvo no mesmo diretório onde se encontra .cdsapirc

####### FIM ###########
