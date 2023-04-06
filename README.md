# Download do espectro horário de ondas gerado por previsão determinística do ERA5-ECMWF
Baixando série horária do espectro de ondas (m2 s radian-1) da previsão determinística do ERA5

Detalhes sobre o acesso ao dado se encontra [aqui](https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation#ERA5:datadocumentation-Parameterlistings).

## Instalando CDS API
Detalhes sobre a instalação do CDS API se encontra [aqui](https://github.com/Dilello/BaixarDadosERA5no-Win10)

## Executando download do espectro horário de ondas gerado por previsão determinística do ERA5-ECMWF
1 - Abrir o arquivo [ERA5_2DwaveSpectra_load.py](https://github.com/Dilello/DownloadERA5_2DWaveSpectra/blob/main/ERA5_2DwaveSpectra_load.py)

2 - Introduzir os limites em latitude e longitude do recorte espacial de interesse;

3 - Intruduzir dados do período de interesse;

Obs.: O arquivo gerado conterá dados de espectro horário de um dia específico e será salvo no mesmo diretório onde foi criado o arquivo com extensão .cdsapirc.
