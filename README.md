# riskii_spiders

<img src = "./images/logo.png" width = "400px">

Esta libreria debe recibir como entrada una instancia de un Scraper o Crawler desarrollado como RiskiiSpiders y retornar en disco la extracción correspondiente.

La obtención del HTML se hace utilizando RiskiiAPI o de manera local con algún engine.

Problems to solve:
- Retry strategies / Times strategies
- Schema definitions
- Concurrency / Parallelims
- Error handling
- Pagination
- Use generators 
- Easy extraction 

Libraries:
- aiohttp
- requests
- responses
- selenium-wire
- zyte-api