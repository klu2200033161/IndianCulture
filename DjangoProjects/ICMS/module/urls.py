from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', loginpage, name='loginpage'),
    path('login1/',login1,name='login1'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('register/', register, name='register'),
    path('sign/',signup1,name='signup1'),
    path('home1/', homepage1, name='homepage1'),
    path('states/', states, name='states'),
    path('historical/', historical, name='historical'),
    path('cdance/',classicaldances,name='classicaldances'),
    path('fest/',festivals,name='festivals'),
    path('foods/',foods,name='foods'),
    path('cdance/',classicaldances,name='classicaldances'),
    path('fest/',festivals,name='festivals'),
    path('foods/',foods,name='foods'),
    path('states/', states, name='states'),
    path('historical/', historical, name='historical'),
    path('states/', states, name='states'),
    path('historical/', historical, name='historical'),
    path('cdance/',classicaldances,name='classicaldances'),
    path('fest/',festivals,name='festivals'),
    path('foods/',foods,name='foods'),
    path('andra/',andhrapradesh,name='andhrapradesh'),
    path('religions/',religions,name='religions'),
    path('lang/',language,name='language'),
    path('andhrac/',andhraclassical,name='andhraclassical'),
    path('andhraf/',andhrafestivals,name='andhrafestivals'),
    path('andhrar/',andhrareligion,name='andhrareligion'),
    path('andhral/',andhralanguage,name='andhralanguage'),
    path('andhrafd/',andhrafoods,name='andhrafoods'),
    path('vedas/', vedas,name='vedas'),
    path('rigveda/',rigveda,name='rigveda'),
    path('map/',map,name='map'),
    path('sama/',samaveda,name='samaveda'),
    path('yajurveda/',yajurveda,name='yajurveda'),
    path('atharvaveda/',atharvaveda,name='atharvaveda'),
    path('punjab/',punjab,name='punjab'),
    path('punjabc/', punjabclassical, name='punjabclassical'),
    path('punjabf/', punjabfestivals, name='punjabfestivals'),
    path('punjabr/', punjabreligion, name='punjabreligion'),
    path('punjabl/', punjablanguage, name='punjablanguage'),
    path('punjabfd/', punjabfoods, name='punjabfoods'),
    path('hp/', hp, name='hp'),
    path('hpc/', hpclassical, name='hpclassical'),
    path('hpf/', hpfestivals, name='hpfestivals'),
    path('hpr/', hpreligion, name='hpreligion'),
    path('hpl/', hplanguage, name='hplanguage'),
    path('hpfd/', hpfoods, name='hpfoods'),
    path('Chandigarh/',Chandigarh, name='Chandigarh'),
    path('Chandigarhc/', Chandigarhclassical, name='Chandigarhclassical'),
    path('Chandigarhf/', Chandigarhfestivals, name='Chandigarhfestivals'),
    path('Chandigarhr/', Chandigarhreligion, name='Chandigarhreligion'),
    path('Chandigarhl/', Chandigarhlanguage, name='Chandigarhlanguage'),
    path('Chandigarhfd/', Chandigarhfoods, name='Chandigarhfoods'),
    path('uttarakhand/',uttarakhand, name='uttarakhand'),
    path('uttarakhandc/', uttarakhandclassical, name='uttarakhandclassical'),
    path('uttarakhandf/', uttarakhandfestivals, name='uttarakhandfestivals'),
    path('uttarakhandr/', uttarakhandreligion, name='uttarakhandreligion'),
    path('uttarakhandl/', uttarakhandlanguage, name='uttarakhandlanguage'),
    path('uttarakhandfd/', uttarakhandfoods, name='uttarakhandfoods'),
    path('Haryana/',Haryana, name='Haryana'),
    path('Haryanac/', Haryanaclassical, name='Haryanaclassical'),
    path('Haryanaf/', Haryanafestivals, name='Haryanafestivals'),
    path('Haryanar/', Haryanareligion, name='Haryanareligion'),
    path('Haryanal/', Haryanalanguage, name='Haryanalanguage'),
    path('Haryanafd/', Haryanafoods, name='Haryanafoods'),
    path('Uttarpradesh/', Uttarpradesh, name='Uttarpradesh'),
    path('Uttarpradeshc/', Uttarpradeshclassical, name='Uttarpradeshclassical'),
    path('Uttarpradeshf/', Uttarpradeshfestivals, name='Uttarpradeshfestivals'),
    path('Uttarpradeshr/',Uttarpradeshreligion, name='Uttarpradeshreligion'),
    path('Uttarpradeshl/', Uttarpradeshlanguage, name='Uttarpradeshlanguage'),
    path('Uttarpradeshfd/', Uttarpradeshfoods, name='Uttarpradeshfoods'),
    path('contact1/',contactmail1,name='contactmail1'),
    path('contact/',contactmail,name='contactmail'),
    path('Sikkim/', Sikkim, name='Sikkim'),
    path('Sikkimc/', Sikkimclassical, name='Sikkimclassical'),
    path('Sikkimf/', Sikkimfestivals, name='Sikkimfestivals'),
    path('Sikkimr/',Sikkimreligion, name='Sikkimreligion'),
    path('Sikkiml/', Sikkimlanguage, name='Sikkimlanguage'),
    path('Sikkimfd/', Sikkimfoods, name='Sikkimfoods'),
    path('Rajasthan/', Rajasthan, name='Rajasthan'),
    path('Rajasthanc/', Rajasthanclassical, name='Rajasthanclassical'),
    path('Rajasthanf/', Rajasthanfestivals, name='Rajasthanfestivals'),
    path('Rajasthanr/', Rajasthanreligion, name='Rajasthanreligion'),
    path('Rajasthanl/', Rajasthanlanguage, name='Rajasthanlanguage'),
    path('Rajasthanfd/', Rajasthanfoods, name='Rajasthanfoods'),
    path('Bihar/', Bihar, name='Bihar'),
    path('Biharc/', Biharclassical, name='Biharclassical'),
    path('Biharf/', Biharfestivals, name='Biharfestivals'),
    path('Biharr/',Biharreligion, name='Biharreligion'),
    path('Biharl/', Biharlanguage, name='Biharlanguage'),
    path('Biharfd/', Biharfoods, name='Biharfoods'),
    path('Jharkhand/', Jharkhand, name='Jharkhand'),
    path('Jharkhandc/', Jharkhandclassical, name='Jharkhandclassical'),
    path('Jharkhandf/', Jharkhandfestivals, name='Jharkhandfestivals'),
    path('Jharkhandr/', Jharkhandreligion, name='Jharkhandreligion'),
    path('Jharkhandl/', Jharkhandlanguage, name='Jharkhandlanguage'),
    path('Jharkhandfd/', Jharkhandfoods, name='Jharkhandfoods'),
    path('Gujarat/', Gujarat, name='Gujarat'),
    path('Gujaratc/', Gujaratclassical, name='Gujaratclassical'),
    path('Gujaratf/', Gujaratfestivals, name='Gujaratfestivals'),
    path('Gujaratr/', Gujaratreligion, name='Gujaratreligion'),
    path('Gujaratl/', Gujaratlanguage, name='Gujaratlanguage'),
    path('Gujaratfd/', Gujaratfoods, name='Gujaratfoods'),
    path('MP/', MP, name='MP'),
    path('MPc/', MPclassical, name='MPclassical'),
    path('MPf/', MPfestivals, name='MPfestivals'),
    path('MPr/', MPreligion, name='MPreligion'),
    path('MPl/', MPlanguage, name='MPlanguage'),
    path('MPfd/', MPfoods, name='MPfoods'),
    path('WB/', WB, name='WB'),
    path('WBc/', WBclassical, name='WBclassical'),
    path('WBf/', WBfestivals, name='WBfestivals'),
    path('WBr/', WBreligion, name='WBreligion'),
    path('WBl/', WBlanguage, name='WBlanguage'),
    path('WBfd/', WBfoods, name='WBfoods'),
    path('religious/',religious,name='religious'),
]

