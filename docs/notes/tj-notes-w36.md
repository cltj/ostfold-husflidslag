# Agile og estimering
Goal: ferdig esimert og prioritert backlog

## manifest for smidig programvareutvikling
- personer go samspill fremfor prosesser og verktøy
- programvare som virker fremfor omfatte4nde dokcs
- samarbeid med kunden fremfor kontraktsforhandlinger
- reagere på endringer romfor å følge plan

### Ut dyping av det smidige manifestet
- Kontinuerlig og tidlig levering av programvare som har verdi til kunden
    - Kunden må føle at de får noe igjen for det som avleveres
- Endring i krav 
- Continuous Delivery
- Daglig samarbeid (scrum)
- Formidle info (snakk sammen face to face) 
- Stadig måle fremdrift
- Bærekraftig programvareutvikling
- Enkelhet (arkitektur)
    - Maksimer arbeid du ikke trenger å gjøre
- De beste arkitekturene, designene og prosessene vokser frem fra selvstyrte team
- Effektivitet, hvordan kan jeg bli bedre



## Roller
- PO = product owner (Arne)
    - har det enedlige ansvaret for backlog
    - samarbeider med kunde for å prioritere (lærer og hjelpelæarer)
    - optimerer verdien utvikler teamet skaper
    - sikrer at backlog er tydelig, transparant og forstått av alle
    - kan delegere deler av arebidet til teamet , men har sluttansvaret
- Development team
    - kryssfunksjonellt
    - selvorganiserte
    - ingen hierarki internt (ikke gjør forskjell på senior og junior)
    - leveranse ansvarlig
    - team størrelse
    - (backend, frontend, arkitektur, testere, devops-rig)
- SM = scrum master (TJ + arkitekt)
    - kan rullere eller ikke
    - har ansvaret for å organiserer sprinten (standup,backlog,måle fremdrift, kommunisere med PO andre interessenter)
- TL = Test Lead (Vu)
    - egen stilling i større organisasjoner/produktteam
    - representeres av en bruker? (Uklar slide)
    - utvikler gjenere automatiserte integrasjonstester
    - 

# Product backlog


## Estimering
- Erfaringsbasert
    - Personlige kunnskap om hvor lang tid detvil ta å gjennomføre et prosjekt eller ferature
    - Krever inngående kjannskap til problemet, eget team og mulige problemer underveis. 
- Algoritmisk
    - Benytter en nøkkelfaktor, antall linje kode, antall krav. eks, og formler for hva dette tilsier i utviklingstid
    - generer et estimat for utviklingstiden
    - Brukes mest innenfor tungt planbaserte miljøer

- T-shirt size (xs,x,m,l,xl,xxl)
- Decomposition and recomposition
    - monolith -> task decomp --> sub-task planning -> action planning


#### Est case
- En restaurant ønsker en enkel mobilapp for bestilling av bord
    - Task 1: Sett opp infrastruktur for app
    - Task 2: Opprette brukerauth
    - Task 3: Bordbestilling


