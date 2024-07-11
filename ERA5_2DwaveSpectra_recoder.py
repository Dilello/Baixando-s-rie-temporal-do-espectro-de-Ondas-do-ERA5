#================================================================================================
# Título: Decodificando espectros de onda 2D no NetCDF
# Fonte: Baseado em códigos fornecidos no site do ERA5
# Autor: Marcelo Di Lello Jordão
# Contato: dilellocn@gmail.com
# Objetivo: Decodificar espectro de onda 2D no NetCDF para latitude, longitude, tempo, frequência (30) e direção (24). 
#=================================================================================================

# BIBLIOTECAS
import xarray as xr
import pandas as pd
import numpy as np

# PERÍODO DE INTERESSE
datas = pd.date_range('2022-8-1','2022-8-31').astype(str)
mes = '08'
ano = '2022'

# DECODIFICANDO O ESPECTRO 
for i in np.arange(0,len(datas)):
    da = xr.open_dataarray('ERA5_DetSpec_'+str(i+1)+mes+ano+'.nc')
    da = da.assign_coords(direction=np.arange(7.5, 352.5 + 15, 15))
    da = da.assign_coords(frequency=np.full(30, 0.03453) * (1.1 ** np.arange(0, 30)))
    da = 10 ** da
    da = da.fillna(0)
    da.to_netcdf(path='ERA5_DetSpec_'+ano+mes+str(i+1)+'_recoded.nc')
####### FIM ###########
