# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#učitavanje fajlova
full = pd.read_csv("full_data.csv")
vacc = pd.read_csv("China.csv")
vaccinations = pd.read_csv("vaccinations.csv")
#%% 1.Analiza Kine
full = full.dropna()
vaccinations = vaccinations.dropna()

#pravimo nove datasetove koji samo sadrže podatke o državama koje analiziramo
full_countries = full.loc[(full["location"] == "China") | (full["location"] == "Italy") | (full["location"] == "India") | (full["location"] == "Spain") | (full["location"] == "Germany"), :]
full_vaccinations = vaccinations.loc[(vaccinations["location"] == "China") | (vaccinations["location"] == "Italy") | (vaccinations["location"] == "India") | (vaccinations["location"] == "Spain") | (vaccinations["location"] == "Germany"), :]

#formiranje dataset-a sa svim podacima o Kini(za ovim nije bilo potrebe ali smo kasnije primetile :D)
full_China = full.loc[(full["location"] == "China"), :]

#konverzija datuma u int
full_China['date'] = full_China['date'].str.replace("-","").astype(int)
 
#Period od 22. januara do 22. maja 2020. (broj zaraženih)
firstSemesterCases2020 = full_China.loc[(full_China["date"] >= 20200122) & (full_China["date"] <= 20200522), "total_cases"]
firstSemesterCases2021 = full_China.loc[(full_China["date"] >= 20210122) & (full_China["date"] <= 20210522), "total_cases"]

plt.figure()
plt.plot(np.arange(1,110),firstSemesterCases2020,"b--", label="2020")
plt.plot( np.arange(1,122),firstSemesterCases2021,"g--", label="2021")
plt.xlabel("broj dana")
plt.ylabel("broj zaraženih")
plt.title("Broj zaraženih u Kini")
plt.legend()


#Period od 22. januara do 22. maja 2020. (broj umrlih)
firstSemesterDeaths2020 = full_China.loc[(full_China["date"] >= 20200122) & (full_China["date"] <= 20200522), "total_deaths"]
firstSemesterDeaths2021 = full_China.loc[(full_China["date"] >= 20210122) & (full_China["date"] <= 20210522), "total_deaths"]

plt.figure()
plt.rcParams['axes.facecolor'] = 'beige'
plt.plot( np.arange(1,110),firstSemesterDeaths2020,"r--", label="2020")
plt.plot( np.arange(1,122),firstSemesterDeaths2021,"g--", label="2021")
plt.xlabel("broj dana")
plt.ylabel("broj umrlih")
plt.title("Broj umrlih u Kini")
plt.legend()


#Broj vakcina prvih mesec dana od postojanja vakcine
totalChina = vacc.loc[(vacc["date"] >= "2020-12-15") & (vacc["date"] <= "2021-01-15"),"total_vaccinations"]
dateChina = vacc.loc[(vacc["date"] >= "2020-12-15") & (vacc["date"] <= "2021-01-15"),"date"]

totalChina = totalChina/1000000

plt.figure()
plt.rcParams['axes.facecolor'] = 'beige'
plt.plot(totalChina, dateChina ,"m--", label="vakcine")
plt.xlabel("broj vakcina u milionima")
plt.ylabel("datum")
plt.title("Broj vakcina u Kini za prvih mesec dana")
plt.legend()


#%% 2.Analiza Italije
full_Italy = full.loc[(full["location"] == "Italy"), :]
vacc_Italy = vaccinations.loc[(vaccinations["location"] == "Italy"), :]
#konverzija datuma u int
full_Italy['date'] = full_Italy['date'].str.replace("-","").astype(int)


#Period od 01. aprila do 26. maja 2020. (broj zaraženih)
firstSemesterCasesI2020 = full_Italy.loc[(full_Italy["date"] >= 20200401) & (full_Italy["date"] <= 20200526), "total_cases"]
firstSemesterCasesI2021 = full_Italy.loc[(full_Italy["date"] >= 20210401) & (full_Italy["date"] <= 20210526), "total_cases"]

firstSemesterCasesI2020 = firstSemesterCasesI2020/1000000
firstSemesterCasesI2021 = firstSemesterCasesI2021/1000000

plt.figure()
plt.rcParams['axes.facecolor'] = 'thistle'
plt.plot(np.arange(1,57),firstSemesterCasesI2020,"b--", label="2020")
plt.plot( np.arange(1,57),firstSemesterCasesI2021,"g--", label="2021")
plt.xlabel("broj dana")
plt.ylabel("broj zarazenih u milionima")
plt.title("Broj zaraženih u Italiji")
plt.legend()


#Period od 01. aprila do 26. maja 2020. (broj umrlih)
firstSemesterDeathsI2020 = full_Italy.loc[(full_Italy["date"] >= 20200401) & (full_Italy["date"] <= 20200526), "total_deaths"]
firstSemesterDeathsI2021 = full_Italy.loc[(full_Italy["date"] >= 20210401) & (full_Italy["date"] <= 20210526), "total_deaths"]

plt.figure()
plt.rcParams['axes.facecolor'] = 'thistle'
plt.plot( np.arange(1,57),firstSemesterDeathsI2020,"g--", label="2020")
plt.plot( np.arange(1,57),firstSemesterDeathsI2021,"r--", label="2021")
plt.xlabel("broj dana")
plt.ylabel("broj umrlih")
plt.title("Broj umrlih u Italiji")
plt.legend()

#Vakcinisani u periodu 27.02 do 27.05.
totalItaly = vacc_Italy.loc[(vacc_Italy["date"] >= "2021-02-27") & (vacc_Italy["date"] <= "2021-05-27"),"people_vaccinated"]
dateItaly = vacc_Italy.loc[(vacc_Italy["date"] >= "2021-02-27") & (vacc_Italy["date"] <= "2021-05-27"),"date"]

totalItaly = totalItaly/1000000

plt.figure()
plt.rcParams['axes.facecolor'] = 'lavender'
plt.plot(np.arange(1,91),totalItaly,"m--", label="vakcine")
plt.xlabel("broj dana")
plt.ylabel("broj vakcinisanih u milionima")
plt.title("Broj vakcinisanih u Italiji")
plt.legend()


#histplot Italija
sns.histplot(data=full_Italy, x="total_cases", y="total_deaths", color='crimson')


#mozda
sns.kdeplot(data=full_Italy, x='new_deaths', y='new_cases',color='forestgreen' )
sns.despine()
#mozda
sns.kdeplot(data=full_Italy, x='date', y='total_cases',color='forestgreen' )
sns.despine()
#mozda
sns.kdeplot(data=full_Italy, x='date', y='total_deaths',color='forestgreen' )
sns.despine()

#prikaz za sve države nove slučajeve zaraženih i smrtne slučajeve
sns.scatterplot(data=full_countries, x='new_deaths', y='new_cases', hue='location' )
sns.despine()

#%% 3.Analiza Indije

#primenjujemo već postojeći dataset
full_India = full_countries.loc[full_countries.location == "India", :]
vacc_India = vaccinations.loc[(vaccinations["location"] == "India"), :]

#pretvaramo date u int
full_India['date'] = full_India['date'].str.replace("-","").astype(int)


#Period od 23. marta do 27. maja 2020. i 2021. godine (broj zaraženih)
firstSemesterCasesIndia2020 = full_India.loc[(full_India["date"] >= 20200323) & (full_India["date"] <= 20200527), "total_cases"]
firstSemesterCasesIndia2021 = full_India.loc[(full_India["date"] >= 20210323) & (full_India["date"] <= 20210527), "total_cases"]

#firstSemesterCasesIndia2020 = firstSemesterCasesIndia2020/1000000
#firstSemesterCasesIndia2021 = firstSemesterCasesIndia2021/1000000

plt.figure()
plt.rcParams['axes.facecolor'] = 'khaki'
plt.plot(np.arange(1,67),firstSemesterCasesIndia2020,"darkgreen", label="2020")
plt.plot( np.arange(1,67),firstSemesterCasesIndia2021,"darkblue", label="2021")
plt.xlabel("broj dana")
plt.ylabel("broj zarazenih u milionima")
plt.title("Broj zaraženih u Indiji")
plt.legend()


#Period od 23. marta do 27. maja 2020. i 2021. godine (broj umrlih)
firstSemesterDeathsIndia2020 = full_India.loc[(full_India["date"] >= 20200323) & (full_India["date"] <= 20200527), "total_deaths"]
firstSemesterDeathsIndia2021 = full_India.loc[(full_India["date"] >= 20210323) & (full_India["date"] <= 20210527), "total_deaths"]


plt.figure()
plt.rcParams['axes.facecolor'] = 'khaki'
plt.plot(np.arange(1,67),firstSemesterDeathsIndia2020,"darkblue", label="2020")
plt.plot( np.arange(1,67),firstSemesterDeathsIndia2021,"r--", label="2021")
plt.xlabel("broj dana")
plt.ylabel("broj umrlih")
plt.title("Broj umrlih u Indiji")
plt.legend()

#Vakcinisani u periodu 27.02 do 27.05.
totalIndia = vacc_India.loc[(vacc_India["date"] >= "2021-03-23") & (vacc_India["date"] <= "2021-05-27"),"people_vaccinated"]
dateIndia = vacc_India.loc[(vacc_India["date"] >= "2021-03-23") & (vacc_India["date"] <= "2021-05-27"),"date"]

totalIndia = totalIndia/1000000

plt.figure()
plt.rcParams['axes.facecolor'] = 'khaki'
plt.plot(np.arange(1,60),totalIndia,"darkgreen", label="vakcine")
plt.xlabel("broj dana")
plt.ylabel("broj vakcinisanih u milionima")
plt.title("Broj vakcinisanih u Indiji")
plt.legend()

#%%4.Analiza Spanije
full_Spain = full.loc[(full["location"] == "Spain"), :]
vacc_Spain = vaccinations.loc[(vaccinations["location"] == "Spain"), :]

#Period od 3. marta do 27. maja 2020. (broj zaraženih)
firstSemesterCasesS2020 = full_Spain.loc[(full_Spain["date"] >= "2020-03-03") & (full_Spain["date"] <= "2020-05-27"), "total_cases"]
firstSemesterCasesS2021 = full_Spain.loc[(full_Spain["date"] >= "2021-03-03") & (full_Spain["date"] <= "2021-05-27"), "total_cases"]

firstSemesterCasesS2020 = firstSemesterCasesS2020/1000000
firstSemesterCasesS2021 = firstSemesterCasesS2021/1000000


plt.figure()
plt.rcParams['axes.facecolor'] = 'thistle'
plt.plot(np.arange(1,87),firstSemesterCasesS2020,"b--", label="2020")
plt.plot( np.arange(1,87),firstSemesterCasesS2021,"g--", label="2021")
plt.xlabel("broj dana")
plt.ylabel("broj zarazenih u milionima")
plt.title("Broj zaraženih u Španiji")
plt.legend()


#Period od 3. marta do 27. maja 2020. (broj umrlih)
firstSemesterDeathsS2020 = full_Spain.loc[(full_Spain["date"] >= "2020-03-03") & (full_Spain["date"] <= "2020-05-27"), "total_deaths"]
firstSemesterDeathsS2021 = full_Spain.loc[(full_Spain["date"] >= "2021-03-03") & (full_Spain["date"] <= "2021-05-27"), "total_deaths"]

plt.figure()
plt.rcParams['axes.facecolor'] = 'thistle'
plt.plot( np.arange(1,87),firstSemesterDeathsS2020,"g--", label="2020")
plt.plot( np.arange(1,87),firstSemesterDeathsS2021,"r--", label="2021")
plt.xlabel("broj dana")
plt.ylabel("broj umrlih")
plt.title("Broj umrlih u Španiji")
plt.legend()

#Broj vakcinisanih u Španiji kroz 4 prva meseca 2021.
totalSpain = vacc_Spain.loc[(vacc_Spain["date"] >= "2021-01-04") & (vacc_Spain["date"] <= "2021-05-27"),"people_vaccinated"]
dateSpain = vacc_Spain.loc[(vacc_Spain["date"] >= "2021-01-04") & (vacc_Spain["date"] <= "2021-05-27"),"date"]

totalSpain = totalSpain/1000000

plt.figure()
plt.rcParams['axes.facecolor'] = 'lavender'
plt.plot(np.arange(1,74),totalSpain,"m--", label="vakcine")
plt.xlabel("broj dana")
plt.ylabel("broj vakcinisanih u milionima")
plt.title("Broj vakcinisanih u Španiji")
plt.legend()
#%%Analiza Nemacke
full_Germany = full.loc[(full["location"] == "Germany"), :]
vacc_Germany = vaccinations.loc[(vaccinations["location"] == "Germany"), :]

#Period od 3. marta do 27. maja 2020. (broj zaraženih)
firstSemesterCasesG2020 = full_Germany.loc[(full_Germany["date"] >= "2020-03-03") & (full_Germany["date"] <= "2020-05-27"), "total_cases"]
firstSemesterCasesG2021 = full_Germany.loc[(full_Germany["date"] >= "2021-03-03") & (full_Germany["date"] <= "2021-05-27"), "total_cases"]

firstSemesterCasesG2020 = firstSemesterCasesG2020/1000000
firstSemesterCasesG2021 = firstSemesterCasesG2021/1000000


plt.figure()
plt.rcParams['axes.facecolor'] = 'thistle'
plt.plot(np.arange(1,81),firstSemesterCasesG2020,"b--", label="2020")
plt.plot(np.arange(1,87),firstSemesterCasesG2021,"g--", label="2021")
plt.xlabel("broj dana")
plt.ylabel("broj zarazenih u milionima")
plt.title("Broj zaraženih u Nemačkoj")
plt.legend()


#Period od 3. marta do 27. maja 2020. (broj umrlih)
firstSemesterDeathsG2020 = full_Germany.loc[(full_Germany["date"] >= "2020-03-03") & (full_Germany["date"] <= "2020-05-27"), "total_deaths"]
firstSemesterDeathsG2021 = full_Germany.loc[(full_Germany["date"] >= "2021-03-03") & (full_Germany["date"] <= "2021-05-27"), "total_deaths"]

plt.figure()
plt.rcParams['axes.facecolor'] = 'thistle'
plt.plot( np.arange(1,81),firstSemesterDeathsG2020,"g--", label="2020")
plt.plot( np.arange(1,87),firstSemesterDeathsG2021,"r--", label="2021")
plt.xlabel("broj dana")
plt.ylabel("broj umrlih")
plt.title("Broj umrlih u Nemačkoj")
plt.legend()

#Broj vakcinisanih u Nemačkoj kroz 4 prva meseca 2021.
totalGermany = vacc_Germany.loc[(vacc_Germany["date"] >= "2021-01-04") & (vacc_Germany["date"] <= "2021-05-27"),"people_vaccinated"]
dateGermany = vacc_Germany.loc[(vacc_Germany["date"] >= "2021-01-04") & (vacc_Germany["date"] <= "2021-05-27"),"date"]

totalGermany = totalGermany/1000000

plt.figure()
plt.rcParams['axes.facecolor'] = 'lavender'
plt.plot(np.arange(1,145),totalGermany,"m--", label="vakcine")
plt.xlabel("broj dana")
plt.ylabel("broj vakcinisanih u milionima")
plt.title("Broj vakcinisanih u Nemačkoj")
plt.legend()

#%%Sve države
#total cases
india = full_countries.loc[full_countries.location == "India", "total_cases"]
italy = full_countries.loc[full_countries.location == "Italy", "total_cases"]
spain = full_countries.loc[full_countries.location == "Spain", "total_cases"]
germany = full_countries.loc[full_countries.location == "Germany", "total_cases"]
china = full_countries.loc[full_countries.location == "China", "total_cases"]


plt.figure()
plt.rcParams['axes.facecolor'] = 'papayawhip'
plt.plot(np.arange(1,444),india,"r--", label="india")
plt.plot(np.arange(1,463),italy,"darkgreen", label="italy")
plt.plot(np.arange(1,452),spain,"lightblue", label="spain")
plt.plot(np.arange(1,446),germany,"gold", label="germany")
plt.plot(np.arange(1,480),china,"m--", label="china")
plt.xlabel("broj dana")
plt.ylabel("broj zarazenih ")
plt.title("Broj zarazenih u svim drzavama")
plt.legend()

#total deaths
indiaD = full_countries.loc[full_countries.location == "India", "total_deaths"]
italyD = full_countries.loc[full_countries.location == "Italy", "total_deaths"]
spainD = full_countries.loc[full_countries.location == "Spain", "total_deaths"]
germanyD = full_countries.loc[full_countries.location == "Germany", "total_deaths"]
chinaD = full_countries.loc[full_countries.location == "China", "total_deaths"]


plt.figure()
plt.rcParams['axes.facecolor'] = 'papayawhip'
plt.plot(np.arange(1,444),indiaD,"r--", label="india")
plt.plot(np.arange(1,463),italyD,"darkgreen", label="italy")
plt.plot(np.arange(1,452),spainD,"lightblue", label="spain")
plt.plot(np.arange(1,446),germanyD,"gold", label="germany")
plt.plot(np.arange(1,480),chinaD,"m--", label="china")
plt.xlabel("broj dana")
plt.ylabel("broj umrlih ")
plt.title("Broj umrlih u svim drzavama")
plt.legend()

#full vaccinations
indiaV = full_vaccinations.loc[full_vaccinations.location == "India", "people_vaccinated"]
italyV = full_vaccinations.loc[full_vaccinations.location == "Italy", "people_vaccinated"]
spainV = full_vaccinations.loc[full_vaccinations.location == "Spain", "people_vaccinated"]
germanyV = full_vaccinations.loc[full_vaccinations.location == "Germany", "people_vaccinated"]
chinaV = full_vaccinations.loc[full_vaccinations.location == "China", "people_vaccinated"]


plt.figure()
plt.rcParams['axes.facecolor'] = 'papayawhip'
plt.plot(np.arange(1,96),indiaV,"r--", label="india")
plt.plot(np.arange(1,132),italyV,"darkgreen", label="italy")
plt.plot(np.arange(1,74),spainV,"lightblue", label="spain")
plt.plot(np.arange(1,152),germanyV,"gold", label="germany")
plt.plot(np.arange(1,1),chinaV,"m--", label="china")
plt.xlabel("broj dana")
plt.ylabel("broj vakcinisanih ")
plt.title("Broj vakcinisanih u svim drzavama")
plt.legend()