# Lecture 2

## Kravspesifikasjon
### Hva er en funksjon

### Hvem er brukeren
- Må prioritere funksjonalitet
- 3-delt brukerbase


Personas: 
- representerer entenkt uker og deres ferdigheterog motivasjon for å benytte programmet
- hvilke funksjonalitet trengs for å tilfredstille personas. 

#### Lag **minst** tre personas...
- Content creator / admin
    -- Rolle: Styremedlem i østfold husflidsslag 
    -- Bakgrunn: Frivillig administrator som opprettholder en interesse og et tilbud i nærområdet. 
    -- Kompetanse: Mer teknisk enn sluttbrukermassen, men er fortsatt svært avhengig av at systemer er lette og bruke samt enkle og navigere. Ønsker ikke å bruke masse tid på relativt enkle oppgaver. KOmpentanse i hvordan økonomien fungerer. hva paingpoints er for sluttbrukere og for andre som har verv i klubben.  
    -- Behov: Trenger et verktøy som lar meg oppdatere nettsiden uten og kunne webutvikling. Enkelhet rundt å veilede brukere.  
    -- Motivajson: Øke brukermassen, bruke mer tid på beltalende kunder og ikke tech, +++
    -- Frustrasjoner: Dagens redigeringsverktøy har mange bokser og begrensninger
«Aktuelt»-seksjonen er vanskelig å oppdatere
Vanskelig å kontrollere hvordan tekst og bilder ser ut
Har ikke tid eller kompetanse til komplisert webadministrasjon


- Sluttbruker
 -- Rolle: Brukere av websiden ( kursholder, kursdelater, medlem, selgere, annonyme brukere)
    -- Bakgrunn: Interessert i huslids-stuff. Gjerne med et skillset som å sy eller lage gjenstander av denne type/kategori. Mye fritid. 
    -- Kompetanse: Skillset es ovenfor... Ikke noen interesse av å drive med teknologi. Facebook kompetanse, og minimalt med www. 
    -- Behov: Holde seg oppdatert på det som skjer. Legge til eller delta på kurs, betale medlemskontigent, selge ting, enkel navingering og gjerne på håndholdte enheter. 
    -- Motivajson: Bedrive sin lidenskap og interesse, samhold og sosialt, 
    -- Frustrasjoner: Synes dagens nettside er rotete. Sliter med å finne kurs og aktuelle aktiviteter. Er usikker på hva som skjer etter at hun betaler for et kurs. Foretrekker tydelig informasjon fremfor fancy design.

- Utvikler 
 -- Rolle: Utvikler 
    -- Bakgrunn: Interesse og arbeider gjerne med utvikling.  
    -- Kompetanse: Dyp teknisk innsikt. 
    -- Behov: Trenger å forstå hvordan prosjektet skal avlevers. Trenger å forstå kunde og kundes kunde behov. 
    -- Motivajson: Penger, prestisje. 
- Drifer
 -- Rolle: Drifter 
    -- Bakgrunn:
    -- Kompetanse:
    -- Behov:
    -- Motivajson:


### Scenario bestanddeler
1. En kort beskrivelse av det overordnede målet
2. referer til persone som er involvert for å få infromasjon om evner samt moticasjon til brukeren
3. info om hva som er involvert for å gjennomføre aktiviteten.
4. En forklaring av problemeer om ikke kan løses i det eksisterende systemet
5. En beskrivelse av en måte problemet kan løses på. 

##### Simuler tenkninig: 
Perona --> Scenario --> Brukeropplevelser 
>![PS!]Skal skrives fra personas sitt perspektiv. 
Ikke forklar implementasjonsinfo, men hvordan systemet skal brukes av den enkelte bruker.

### Scenario per persona:
- Admin: 
    -- Overordnet mål: Fasilitere kurs, drive interesenter til websiden, 
Scenario1: Publisere et nytt kurs

Anne er 61 år og frivillig administrator for det lokale Husflidslaget. Hun har fått informasjon fra en kursleder om et nytt kurs som skal arrangeres om noen uker.

Hun logger inn på nettsiden for å publisere informasjonen. Hun må fylle ut flere forskjellige felt og opplever at hun har liten kontroll over hvordan tekst og bilder blir presentert. Hun ønsker å legge inn flere bilder fra tidligere kurs, men dagens løsning gjør dette vanskelig.

Etter å ha publisert innlegget ønsker hun også at informasjonen skal være lett synlig under «Aktuelt», slik at medlemmene raskt oppdager det nye kurset.

Mål: Få informasjon om kurset raskt og tydelig ut til medlemmene.

Problem: Publiseringsverktøyet er tungvint og begrensende.

«Jeg vet hva jeg vil fortelle medlemmene, men nettsiden gjør det unødvendig vanskelig å få det ut.»

- Sluttbruker:
Scenario1: Finne og melde seg på et kurs

Kari er 68 år og har nylig blitt pensjonist. Hun har lyst til å lære seg en ny teknikk innen strikking og ønsker samtidig å møte andre med samme interesse. Hun har hørt at det skal arrangeres et kurs gjennom det lokale Husflidslaget.

På kvelden setter hun seg ved PC-en og går inn på nettsiden. Hun ønsker å finne ut når kurset er, hvor det holdes, hvor mange plasser som er ledige og hva det koster.

Hun opplever imidlertid at nettsiden er litt rotete og bruker tid på å finne frem til riktig kurs. Når hun først finner kurset, blir hun usikker på hva som skjer dersom hun melder seg på og betaler, men kurset senere blir avlyst eller hun selv blir syk.

Mål: Finne riktig kurs og melde seg på med trygghet.

Problem: Vanskelig navigasjon og usikkerhet rundt påmelding og betaling.

«Jeg vil bare finne kurset jeg er interessert i, og vite at det er trygt å melde seg på.»


- Utvikler:
    -- Scenario1:
Markus skal videreutvikle løsningen

Markus får beskjed om at Husflidslaget ønsker en ny funksjon for kursadministrasjon. Før han begynner å utvikle funksjonen, må han forstå hvordan dagens system håndterer brukere, kurs og påmeldinger.

Han undersøker dokumentasjonen og kildekoden og ønsker å kjøre eksisterende tester før han gjør endringer. Etter implementeringen kjører han testene på nytt og gjennomfører code review sammen med resten av utviklergruppen.

Underveis oppdager han at en endring i kursmodulen kan påvirke andre deler av systemet. Fordi systemet har tydelige komponenter og gode tester, kan han identifisere problemet før endringen blir satt i produksjon.

Mål: Videreutvikle systemet på en trygg og kontrollert måte.

Problem: Dårlig struktur, dokumentasjon eller testing kan gjøre videreutvikling risikabelt.

«Jeg må kunne endre systemet uten å være redd for å ødelegge noe jeg ikke visste var avhengig av endringen.»


- Drifter:

#### Brukerhistorier: 
//- Som en sideadministrator ønsker/trenger jeg å kommunisere til kursdeltagere når det er endinger slik at innvollverte føler seg oppdaterte på forhånd.//


- Som en webadministrator ønsker/trenger jeg å publisere informasjon på websiden på en måte som brukere naturlig oppdager nytt innhold. 
    -- Tydelig definert funksjon: 
    -- Product backlog ( samling av brukerhistorier):
    -- Epic ( omfattende brukerhistorie, kan bli delt opp i mindre brukerhistorier):

- Brukerhistorie for webadministrator: 

Som webadministrator ønsker jeg å kunne opprette et nytt innlegg i «Aktuelt», slik at jeg enkelt kan informere medlemmene om nyheter og oppdateringer.

Hvorfor denne passer kriteriene
Rolle: Administrator
Ønsker: Opprette et nytt innlegg
Handling: Én tydelig funksjon
Grunn: Informere medlemmene
Avgrenset: Kan implementeres og testes innenfor én sprint
Funksjonsidentifikasjon: Gir dere en konkret funksjon → opprette innlegg i Aktuelt

Da kan dere eventuelt lage separate brukerhistorier for funksjoner som:

Som administrator ønsker jeg å kunne legge til bilder i et innlegg, slik at jeg kan gjøre informasjonen mer relevant og visuelt forståelig for medlemmene.

Som administrator ønsker jeg å kunne redigere et publisert innlegg, slik at jeg kan korrigere eller oppdatere informasjon.

Som administrator ønsker jeg å kunne forhåndsvise et innlegg før publisering, slik at jeg kan kontrollere hvordan innholdet ser ut for brukerne.

Disse kan igjen samles under en Epic, for eksempel:

Epic: Administrere «Aktuelt»
- Opprette innlegg
- Legge til bilder
- Redigere innlegg
- Forhåndsvise innlegg
- Publisere innlegg
- Slette innlegg

---

Hovedhistorie Kari:

Som kursdeltaker ønsker jeg å kunne søke og filtrere frem kurs på nettsiden, slik at jeg enkelt finner kurset jeg er interessert i.

Hvorfor denne passer kriteriene

Rolle: Kursdeltaker (potensiell bruker, f.eks. Kari). Ønsker: Søke og filtrere frem kurs. Handling: Én tydelig funksjon. Grunn: Finne riktig kurs uten å måtte lete seg gjennom en rotete nettside. Avgrenset: Kan implementeres og testes innenfor én sprint. Funksjonsidentifikasjon: Gir dere en konkret funksjon → søk/filter for kurs.

Da kan dere lage separate brukerhistorier for de andre behovene som kommer frem i scenarioet:

Som kursdeltaker ønsker jeg å se detaljert informasjon om et kurs (dato, sted, antall ledige plasser og pris), slik at jeg kan vurdere om jeg vil melde meg på.

Som kursdeltaker ønsker jeg å melde meg på et kurs direkte fra kurssiden, slik at jeg raskt kan sikre meg en plass.

Som kursdeltaker ønsker jeg å se vilkårene for avbestilling og refusjon før jeg betaler, slik at jeg vet hva som skjer dersom kurset avlyses eller jeg selv blir syk.

Som kursdeltaker ønsker jeg å motta en bekreftelse (f.eks. på e-post) etter påmelding, slik at jeg er trygg på at plassen min er registrert.

Epic: Finne og melde seg på kurs
- Søke og filtrere kurs
- Se kursdetaljer (dato, sted, plasser, pris)
- Melde seg på kurs
- Se vilkår for avbestilling/refusjon
- Motta bekreftelse på påmelding

---

Brukerhistorie Utvikler:
Hovedhistorie:
Som utvikler ønsker jeg å kunne kjøre automatiserte tester for kursmodulen, slik at jeg kan kontrollere at endringene mine ikke ødelegger eksisterende funksjonalitet.

Hvorfor denne passer kriteriene

Rolle: Utvikler
Ønsker: Kjøre automatiserte tester
Handling: Én tydelig funksjon
Grunn: Oppdage feil og regresjoner før produksjonssetting
Avgrenset: Kan implementeres og testes innenfor én sprint
Funksjonsidentifikasjon: Gir en konkret funksjon → kjøre automatiserte tester for kursmodulen

Da kan dere lage separate brukerhistorier for funksjoner som:

Som utvikler ønsker jeg å kunne finne dokumentasjon om kursmodulens oppbygning, slik at jeg raskt kan forstå hvordan brukere, kurs og påmeldinger henger sammen.

Som utvikler ønsker jeg å kunne sette opp og kjøre systemet lokalt, slik at jeg kan undersøke eksisterende funksjonalitet før jeg gjør endringer.

Som utvikler ønsker jeg å kunne kjøre integrasjonstester mellom kursmodulen og brukermodulen, slik at jeg kan oppdage om en endring påvirker andre deler av systemet.

Som utvikler ønsker jeg å kunne se hvilke komponenter som er avhengige av kursmodulen, slik at jeg kan vurdere konsekvensene av en endring.

Som utvikler ønsker jeg at endringene mine automatisk bygges og testes, slik at feil oppdages før koden slås sammen.

Som utvikler ønsker jeg å kunne sende endringene mine til code review, slik at utviklergruppen kan kvalitetssikre løsningen før den settes i produksjon.

Som utvikler ønsker jeg å kunne lese dokumentasjon om hvordan løsningen skal leveres, slik at jeg kan følge prosjektets krav til bygging og produksjonssetting.

Disse kan samles under følgende epic:

Epic: Trygg videreutvikling av kursløsningen
Forstå kursmodulens oppbygning
Sette opp løsningen lokalt
Kjøre eksisterende tester
Teste avhengigheter mellom komponenter
Identifisere berørte komponenter
Kjøre automatisk bygg og testing
Gjennomføre code review
Dokumentere endringer og leveranse


---


#### Funksjonsidentifikasjon
- Feature/ funksjon
    -- Uavhengighet:Hver enkelt funksjon skal kunne stå på egne ben. Skal kunne gjøre endringer uavhengig av andre. 
   -- Sammenheng: Funksjoner ska lvære knuttet itl et enkelt funksjsonelement. Funksjoner bør ikke gjøre mer enn en ting, og de bør alrdi ha bivirkninger. 
    -- Relevans: Funksjoner bør gjenspeile måten .....?? 

#### Funksjons avveininger.
- Enkelhet og funksjonalitet- så enkelt som mulig åbruke og på samme tid innehodle funksjonalitet som lar brukerne gjøre det de ønsker. 
- Kjennskap og mnyhet - støtte for kjente hversagsoperasjoner og på asmme tid innføre nye funksjoner som over beviser brukerne om å bytte system. 
- Automatisering og kontroll - automatisere arbeidsoppaver for brukerne samtidig som de må føle kontroll selv. 


#### Funksjonelle og ikke-funksjonelle krav
- Funksjonelle krav: det du kan teste (unit tests) 
- Ikke-funksjonelle krav: Driftskrav, oppetid osv


### hva er et krav? 
Kravene til et system er funksjonene et system skal tilby, samme med  begrensningerav systemet.Kravene beskrivelse behovene brukerne har til systemet for å gjennomføre spesifikke oppgaver. 
- En fullverdig kravspec
    - Deretter triage
        - Må, bør, kan



#### Lag deres kravspec: 
- webadministrator:
Epic: Administrere «Aktuielt»

| ID | Funksjon | Brukerhistorie (kort) | Funksjonelt krav | Prioritet |
|----|----------|------------------------|-------------------|-----------|
| F1 | Opprette innlegg | Som administrator ønsker jeg å opprette et nytt innlegg, slik at jeg kan informere medlemmene om nyheter. | Systemet skal la administrator opprette et innlegg med tittel og brødtekst, og lagre det som kladd. | Må |
| F2 | Legge til bilder | Som administrator ønsker jeg å legge til bilder i et innlegg, slik at informasjonen blir mer relevant og visuelt forståelig. | Systemet skal la administrator laste opp og plassere ett eller flere bilder i et innlegg. | Bør |
| F3 | Redigere innlegg | Som administrator ønsker jeg å redigere et publisert innlegg, slik at jeg kan korrigere eller oppdatere informasjon. | Systemet skal la administrator endre tittel, tekst og bilder i et allerede publisert innlegg. | Må |
| F4 | Forhåndsvise innlegg | Som administrator ønsker jeg å forhåndsvise et innlegg før publisering, slik at jeg kan kontrollere hvordan innholdet ser ut for brukerne. | Systemet skal vise en forhåndsvisning av innlegget slik det vil se ut publisert, uten at det er synlig for andre brukere. | Bør |
| F5 | Publisere innlegg | Som administrator ønsker jeg å publisere et innlegg, slik at det blir synlig for medlemmene. | Systemet skal la administrator gjøre et kladd-innlegg synlig på «Aktuelt»-siden for alle brukere. | Må |
| F6 | Slette innlegg | Som administrator ønsker jeg å slette et innlegg, slik at utdatert eller feilaktig innhold ikke ligger igjen. | Systemet skal la administrator fjerne et innlegg permanent, med en bekreftelsesdialog før sletting. | Kan |




- sluttbruker:
kommer


- utvikler:
kommer


## Prosessmodell (neste modell) 
- Hvilke faser og aktivieterer bestpr prosjektet av? 
- Hvilke avhengigheter er et mellom disse? 
- Når gjennomføres den? 

Kundemøte --> Kravspesifikasjon --> validering av krav --> beskrivelse av systemet --> utvikling --> testing --> integrasjon --> drift --> vedlikehold


##### Når er fossefall nyttig? 
- Kritiske systemer som krever detaljert sikekrhts og trygghetsanalyse, av spesifikasjon og design av programvaren. 
- Situasjoner hvor mange selskap, tilbydere eller team er involvert 

HVA OM VI OMBESTEMMER OSS? 
- Det er ikke umulig å gå bakover i prosessen, men det kan være omstendelig og kostbar prosess med hensyn på tidsbruk, etc. 
Typsiske problemer: Verden endrer seg, kunden vet ikke hva behovedt er , under utvikling oppdages andre utfordringer, produktivitet vs byråkrati, krever god erfaring og trygg arkitektur.

##### Smidig utvikling
krav --> arkitektur --> utvikling --> testing --> ??? 
- Always be delivering!! 
utfordringer:
- Interne begrensninger
- Byråkratiske oppgaver
- Prosess
- Endringer


AIM SMALL MISS SMALL!!!!






