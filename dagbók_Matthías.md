## 18.04.2018 
#### Setti upp seinni serverinn, setti upp static IP fyrir hann, DHCP og NAT, tengdi tölvurnar við domainið sem Sveinn setti upp.

## 20.04.2018 
#### Setti upp home folderin fyrir nemendur og kennara upp á seinni serverinum og bætti við quota á folderin þannig að nemendur eru með 10MB og kennarar með 20MB. Ég náði líka í BGInfo og gerði öll skjöl tilbúin og script fyrir Svein til að bæta við í GPO.

## 25.04.2018 
#### Settu upp ftp server á seinni serverinum og var að prufa stillingar fyrir hann endaði með að setja hann upp þannig að allir kennarar geta notað ftp til þess að fá aðgang að root web serversins og hafa read + write þar.

## 27.04.2018
#### Setti upp mysql og phpmyadmin og bjó til python forrit sem fer í gegnum csv skjalið og bætir við kennurum með usernameinu sem er í csv skjalinu og lykilorðið pass.123 og er hægt að tegnjast með workbench eða phpmyadmin á 10.201.190.87/phpmyadmin kennararnir eru lokaðir af og geta aðeins haft aðgang að databaseum sem eru staðsettir undir notandanafniÞeirra_databaseNafn

## 02.05.2018
#### Bætti við að allir notendur hafa account á mysql serverinum og geta annað hvort tengst með phpmyadmin eða workbench og var að leita af hlutum til þess að bæta við serverina og prufaði nokkra hluti. Kveikti líka á BranchCache sem vistar skjöl frá netinu þegar notendur eru að sækja eitthvað þaðan og ef notandi ætlar að ná í skjal af netinu sem serverinn hefur nú þegar vistað þá gefur serverinn þau frekar locally frá sér í stað þess að downloada aftur skjalinu.
