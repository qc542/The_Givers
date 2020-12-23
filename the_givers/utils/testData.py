# images has to have the form: <id>.png
charities = [
    [
        420,
        "RedCross",
        "We're sorry if our logo gives you PTSD about math.",
        [],
        "420.png",
    ],
    [421, "Humane Society", "It's <i>humane</i> not human.", [], "421.png"],
    [422, "World Wildlife Fund", "Our logo says <b>WWF</b> not WTF.", [], "422.png"],
    [
        423,
        "UNICEF",
        "Treat or treat for UNICEF (if you know, you know)",
        [],
        "423.png",
    ],
    [
        424,
        "AmnestyInternational",
        "<i>We can't expect God to do all the work</i> -Joshua Graham (<i>Fallout: New Vegas</i>)",
        [],
        "424.png",
    ],
]

imageIdByCharityName = {
    "Red-Cross": 420,
    "Humane-Society": 421,
    "UNICEF": 423,
    "Amnesty-International": 424,
    "Food-Bank-For-New-York-City": 69,
}

newsByCharityName = {
    "Red-Cross": [
        [
            "Philippines' Duterte promises payment as Red Cross stops COVID-19 tests - Reuters India",
            "Philippines' Duterte promises payment as Red Cross stops COVID-19 tests\xa0\xa0Reuters India",
        ],
        [
            "Belgium needs plasma to continue COVID-19 studies, Red Cross says - Reuters India",
            "Belgium needs plasma to continue COVID-19 studies, Red Cross says\xa0\xa0Reuters India",
        ],
        [
            "Four dead, several injured in Beirut fuel tank explosion - Reuters",
            "Four people were killed and several more were wounded when a fuel tank exploded in a Beirut building on Friday, the Lebanese Red Cross said.",
        ],
        [
            "Spain's Canary Islands see new influx of African migrants",
            "More than 1,000 have arrived in recent days and this year has seen a big increase from 2019.",
        ],
        [
            "France church attacker was carrying Italian Red Cross ID - prosecutor - Reuters",
            "The man suspected of killing three people in a French church arrived by train carrying an Italian Red Cross identity document, changed his clothes at the train station, then walked to the church to begin his attack, a prosecutor said on Thursday.",
        ],
        [
            "France church attacker was carrying Italian Red Cross ID - prosecutor - Reuters UK",
            "The man suspected of killing three people in a French church arrived by train carrying an Italian Red Cross identity document, changed his clothes at the train station, then walked to the church to begin his attack, a prosecutor said on Thursday.",
        ],
        [
            "Canary Islands sees biggest migrant surge since 2006 - Reuters UK",
            "More than 1,000 migrants reached the Canary Islands in the past 48 hours, the Red Cross said on Saturday, the largest number since a 2006 crisis in the archipelago.",
        ],
        [
            "Yemen's warring parties start swap of 1,000 prisoners - Reuters Canada",
            "Planes carrying prisoners exchanged by the warring parties in Yemen took off from three airports on Thursday in an operation to return about 1,000 men home across the front lines, the International Committee of the Red Cross said.",
        ],
        [
            "Philippines' Duterte promises payment as Red Cross stops COVID-19 tests - Reuters",
            "Philippine President Rodrigo Duterte said on Friday his government will pay the 931 million pesos ($19.25 million) it owes the Red Cross after the humanitarian agency stopped conducting COVID-19 tests.",
        ],
        [
            "Red Cross says boat carrying aid attacked in Myanmar's Rakhine state - Reuters",
            "The International Committee of the Red Cross said on Wednesday a boat carrying its aid in Myanmar's restive Rakhine State had come under attack, in an incident in which the army said it was returning fire from insurgents.",
        ],
        [
            "Nigerian police pledge ICRC training as thousands protest nationwide - Reuters Canada",
            "The International Committee of the Red Cross (ICRC) will help train Nigeria's new tactical force as thousands nationwide continued to march against police brutality and in demand of further reforms, Nigeria's police inspector general said in a statement on Su…",
        ],
        [
            "Nigerian police pledge ICRC training as thousands protest nationwide - Reuters",
            "The International Committee of the Red Cross (ICRC) will help train Nigeria's new tactical force as thousands nationwide continued to march against police brutality and in demand of further reforms, Nigeria's police inspector general said in a statement on Su…",
        ],
        [
            "Red Cross urges Armenia, Azerbaijan to firm up prisoner, body swap - Reuters",
            "The International Committee of the Red Cross urged Armenia and Azerbaijan on Tuesday to finalize arrangements for it to handle an exchange of detainees and bodies from the Nagorno-Karabakh conflict, after a humanitarian ceasefire agreed at the weekend.",
        ],
        [
            "Yemen's largest prisoner swap to go ahead on Thursday - ICRC - Reuters.com",
            "Planes carrying prisoners exchanged by the warring parties in Yemen are set to take off on Thursday in an operation to return about 1,000 men home across the front lines, the International Committee of the Red Cross (ICRC) said.",
        ],
        [
            "Yemen's largest prisoner swap to go ahead on Thursday: ICRC - Reuters",
            "Planes carrying prisoners exchanged by the warring parties in Yemen are set to take off on Thursday in an operation to return about 1,000 men home across the front lines, the International Committee of the Red Cross (ICRC) said.",
        ],
        [
            "Belgium needs plasma to continue COVID-19 studies, Red Cross says - Reuters",
            "Belgian clinical studies to study the effectiveness of blood plasma for people recovering from COVID-19 are at risk of being suspended because of low plasma stocks, doctors said, prompting a call for more blood donors to come forward.",
        ],
        [
            "Vietnam faces deadly flooding disaster - Red Cross",
            "Floodwaters have killed over 100 and left homes submerged, crops destroyed and livestock swept away.",
        ],
        [
            "Typhoon Molave: Landslides kill at least 19 after heavy rain in Vietnam",
            "Dozens are still missing after Typhoon Molave struck central Vietnam, lashing it with wind and rain.",
        ],
        [
            "Channeling 'anger into art', artists in Beirut process blast - Reuters UK",
            "Channeling 'anger into art', artists in Beirut process blast\xa0\xa0Reuters UK",
        ],
        [
            "Canary Islands sees biggest migrant surge since 2006 - Reuters",
            "Canary Islands sees biggest migrant surge since 2006\xa0\xa0Reuters",
        ],
    ],
    "Humane-Society": [
        [
            "Skateboarding TikTok Star Nathan Apodaca Gets Another Big Break - HuffPost Canada",
            "<ol><li>Skateboarding TikTok Star Nathan Apodaca Gets Another Big Break\xa0\xa0HuffPost Canada\r\n</li><li>Courteney Cox Recreates Viral 'Dreams' TikTok With Roller Skates & Cranberry Juice\xa0\xa0Access Hollywood\r\n</li><li>The Best Canadian Versions of the “Dreams” TikTok…",
        ],
        [
            "Hand over the trash: raccoons break into California bank",
            "Pair were noticed causing havoc inside bank by customer withdrawing money outside the buildingTwo “masked” intruders broke into a California bank using a method straight out of the movies: crawling along air ducts – only to fall through the ceiling tiles and …",
        ],
        [
            "Masked Intruders Break Into Bank",
            "An ATM user outside a Redwood City, California, bank noticed that there were things going on inside the closed lobby. Two young raccoons were trapped inside, apparently after climbing through the air ducts to get into the bank. Bank managers and staff from th…",
        ],
        [
            "‘It’s important for the political world of today to own up to their mistakes in public’",
            "Carnatic classical vocalist TM Krishna’s 'The Edict Project' will musically attempt to rediscover King Ashoka’s famed edicts -- philosophies that speak of a more humane society built on empathy and compassion",
        ],
        [
            "'The cougar guy': Utah hiker encounters a cougar who followed him for nearly six minutes",
            "Kyle Burgess of Orem, Utah, stopped to record cubs he saw during his evening run. He was soon being followed by a mother cougar for nearly six minutes.",
        ],
        [
            "Farewell, Fido: U.S. cities see boom in pet cemeteries - Reuters.com",
            "When Jim LaMar's border collie, KC, died in 2012, he had her cremated and kept the remains with him in his California home.",
        ],
        [
            "Elderly shelter pets getting adopted in the coolest way (34 Photos)",
            "The Flagler Humane Society did a photoshoot with their elderly cats and dogs in order to help them get adopted",
        ],
        [
            "Animal Humane Society CEO Janelle Dixon garners 2020 Women in Business award - Minneapolis / St. Paul Business Journal",
            "Animal Humane Society CEO Janelle Dixon garners 2020 Women in Business award\xa0\xa0Minneapolis / St. Paul Business Journal",
        ],
        [
            "TX Family's Dog Stolen 6 Years Ago -- Found In Florida...",
            "TX Family's Dog Stolen 6 Years Ago -- Found In Florida...\r\n\n \n \n \n (Third column, 15th story, link)",
        ],
        [
            "2021 Pooping Dogs Calendar Is Here, and This Year Contains a Puzzle",
            "White Elephant Party coming up? Yankee Swap? Secret Santa? Do you know someone who loves dogs...too much? This 12 month calendar of pooping dogs will be the most memorable gift you give this year. \r\n\r\nTalk about a gift that keeps on giving; each month reveals…",
        ],
        [
            "Raccoons break into bank...",
            'Two young raccoons were caught "breaking into" a California bank, living up to their masked bandit reputation.',
        ],
        [
            "Nordstrom to end the sale of fur and animal skins",
            "One of America's leading fashion retailers, Nordstrom, has announced that it will be ending the sale of fur and animal skins by 2021. This move comes at a time when the world is faced with various environmental issues that are forcing many people to rethink t…",
        ],
        [
            "Nordstrom to stop selling fur and exotic animal skins by the end of 2021",
            "<p>Humane Society hopes move will have a ripple effect on other fashion leaders</p>",
        ],
        [
            "Nordstrom to stop selling fur, exotic animal skin products",
            "Upscale retailer is first in the nation to ban skins from kangaroos, snakes and alligators, Humane Society says.",
        ],
        [
            "'Real and imminent' extinction risk to whales",
            "A letter signed by hundreds of scientists calls for global action to protect whales, dolphins and porpoises.",
        ],
        [
            "'Real and imminent' extinction risk to whales",
            "A letter signed by hundreds of scientists calls for global action to protect whales, dolphins and porpoises.",
        ],
        [
            "'Sheer anxiety': Louisiana braces itself for Hurricane Delta",
            "Louisiana residents still recovering from the devastation of a powerful hurricane less than two months ago braced for another hit as Hurricane Delta steamed north through the Gulf on Thursday after swiping Mexico's Yucatan Peninsula.",
        ],
        [
            "Nordstrom Will No Longer Sell Fur and Exotic-Animal Skins",
            "It’s the first U.S. retailer to ban the latter.",
        ],
        [
            "U.S. Lab Chimps Stuck in Retirement Limbo",
            "Activists and some congressional lawmakers are demanding that the N.I.H. reconsider its refusal to move 39 chimpanzees from a research center to a sanctuary.",
        ],
        [
            "Doc Antle of ‘Tiger King’ Is Charged With Wildlife Trafficking",
            "Mr. Antle’s daughters and a former roadside zoo owner in Virginia also face charges of animal cruelty.",
        ],
    ],
    "UNICEF": [
        [
            "UNICEF Plans to Stockpile Syringes in Preparation for First Vaccines",
            "The U.N. agency said it was amassing medical equipment to be ready when the time comes. Total global virus cases surpassed 40 million. Here’s the latest.",
        ],
        [
            "U.N.'s IOM and UNICEF vow to investigate 'jobs-for-sex' claims in Congo - Reuters India",
            "Two more U.N. agencies joined the World Health Organization (WHO) with pledges on Wednesday to investigate claims of sexual exploitation by aid workers in the Democratic Republic of Congo uncovered by the Thomson Reuters Foundation and The New Humanitarian.",
        ],
        [
            "U.N.'s IOM and UNICEF vow to investigate 'jobs-for-sex' claims in Congo - Reuters",
            "Two more U.N. agencies joined the World Health Organization (WHO) with pledges on Wednesday to investigate claims of sexual exploitation by aid workers in the Democratic Republic of Congo uncovered by the Thomson Reuters Foundation and The New Humanitarian.",
        ],
        [
            "Moncler pledges carbon neutrality by 2021, recycling in new plan - Reuters",
            "Luxury puffer jacket maker Moncler <MONC.MI> committed on Thursday to making production sites carbon-neutral by 2021 and said it would start using from January certified recycled down, in a process requiring 70% less water than the traditional one.",
        ],
        [
            "NZ election: The people left behind in Ardern's 'kind' New Zealand",
            "Critics say Jacinda Ardern has not done enough to combat child poverty as she seeks another term.",
        ],
        [
            "New mom Katy Perry checks out $4M Santa Barbara beach home as she seeks nest for 1-month-old daughter Daisy - The Sun",
            "<ol><li>New mom Katy Perry checks out $4M Santa Barbara beach home as she seeks nest for 1-month-old daughter Daisy\xa0\xa0The Sun\r\n</li><li>Jane Fonda leads celebrity workout class to encourage voting\xa0\xa0The Independent\r\n</li><li>Jane Fonda back to her eighties work…",
        ],
        [
            "Muere Quino, el creador de Mafalda, a los 88 años",
            "Ha muerto Joaquín Salvador Lavado Tejó, mejor conocido como Quino, creador de Mafalda y uno de los artistas más reconocidos de Argentina. La noticia fue confirmada por su editor, Daniel Davisnky en redes sociales. Según informaciones publicadas por medios loc…",
        ],
        [
            "The Campaign To Wipe Out Polio Was Going Really Well ... Until It Wasn't",
            'It looked as if polio would be the second human disease to be eliminated — after smallpox. But "2020 has been a terrible year," says Michel Zaffran, head of the Global Polio Eradication Initiative.',
        ],
        [
            "Kurdish official says thousands of Syrians to leave crowded camp in northeast - Reuters",
            "Kurdish-led authorities said on Monday up to 15,000 Syrians could be moved out of the overcrowded al-Hol camp in northeast Syria which holds displaced people and families of Islamic State fighters.",
        ],
        [
            "Congo to investigate 'jobs-for-sex' accusations during Ebola outbreak - Reuters",
            "Congo to investigate 'jobs-for-sex' accusations during Ebola outbreak\xa0\xa0Reuters",
        ],
        [
            "Jamaican teacher turns Kingston walls into blackboards - Reuters UK",
            "With most schools in Jamaica still closed due to the pandemic, schoolteacher Taneka Mckoy every day braves the risk of stray gunshots from gang warfare and the oppressive Caribbean heat as she trudges around her inner city Kingston community to write lessons …",
        ],
        [
            "Kenya partially reopens schools, six months after COVID closed them - Reuters India",
            "Kenyan schoolchildren in grades four, eight and 12 returned to class on Monday, ending a months-long closure of all educational institutions in the country designed to slow the spread of the novel coronavirus.",
        ],
        [
            "Kurdish official says thousands of Syrians to leave crowded camp in northeast - Reuters UK",
            "Kurdish-led authorities said on Monday up to 15,000 Syrians could be moved out of the overcrowded al-Hol camp in northeast Syria which holds displaced people and families of Islamic State fighters.",
        ],
        [
            "UK bans sex between government aid workers and recipients to rein in abuse - Reuters",
            "Britain has banned sexual relations between government staff giving aid and people receiving it, as lawmakers seek to stamp out abuse in the aid sector following a string of sex scandals.",
        ],
        [
            "Kenya partially reopens schools, six months after COVID closed them - Reuters India",
            "Kenyan schoolchildren in grades four, eight and 12 returned to class on Monday, ending a months-long closure of all educational institutions in the country designed to slow the spread of the novel coronavirus.",
        ],
        [
            "Overstretched health visitors caring for up to 2,400 families each",
            "Exclusive: concerns for mental health and breastfeeding rates owing to already overstretched service in England<ul><li>Alone and in pain: one woman’s struggle for support</li></ul>Overstretched health visitors have been forced to care for up to 2,400 families…",
        ],
        [
            "Facebook bans ads that discourage people from getting vaccines",
            "Facebook will start banning ads that explicitly discourage people from getting vaccinated, the world's largest social media company said on Tuesday.",
        ],
        [
            "COVID-19 Has Robbed The World's Poorest Children Of Nearly 4 Months Of Schooling",
            "A new report finds the return to education has been much slower in the world's poorer countries.",
        ],
        [
            "Facebook is finally banning anti-vax ads from its platform and Instagram",
            "Anti-vaxxers must be steaming. In an effort to curb health misinformation amidst the coronavirus pandemic, Facebook has revealed it’ll start purging ads that discourage vaccines and immunization on its platform and Instagram. As the Wall Street Journal notes,…",
        ],
        [
            "Kinderhilfswerk: Corona: Unicef lagert 520 Millionen Spritzen für Impfung ein",
            "",
        ],
    ],
    "Amnesty-International": [
        [
            "Prison set on fire in Nigeria as protest death toll rises to at least 56",
            "At least 56 people have died across Nigeria since the #EndSARS protests began on October 8, with 38 killed across the country on Tuesday alone, according to human rights group Amnesty International.",
        ],
        [
            "Political failings put Colombian activists at risk: Amnesty - Reuters",
            "Frequent threats, attacks and killings targeting local activists across Colombia highlight the government's inability to protect human rights defenders, advocacy group Amnesty International said on Thursday.",
        ],
        [
            "Non-profits say India's new rules on foreign funding will hit operations - Reuters",
            "India's tougher rules on foreign funding for non-profits will severely crimp their activities, the chiefs of some bodies said on Thursday, after human rights group Amnesty International suspended its work in the country, citing government harassment.",
        ],
        [
            "Amnesty disputes Nigerian army claim it did not shoot Lagos civilians - Reuters India",
            "Nigeria's Lagos state government asked the army to intervene to restore order amid anti-police brutality protests, but soldiers did not shoot civilians, the military said, an assertion an Amnesty International investigation disputed on Wednesday.",
        ],
        [
            "What's Happening in Nigeria?",
            "After a summer of ongoing protests over police violence—including the murders of George Floyd and Breonna Taylor—greater numbers of Americans are starting to understand this facet of systemic racism. Of course, it’s not only an issue in the United States, and…",
        ],
        [
            "Afghan-Taliban conflict: Fears grow for families trapped in Helmand",
            "Aid groups say civilians must be given safe passage amid clashes between Taliban and government forces.",
        ],
        [
            "Nigerian president criticised over response to protests crackdown",
            "Muhammadu Buhari urged to address nation after shootings by security forces on Tuesday Nigeria’s president, Muhammadu Buhari, has been criticised for his muted response after security forces opened fire on people protesting against police brutality in Lagos o…",
        ],
        [
            "Poland abortion: Top court to rule on almost total ban",
            "Poland has some of Europe's strictest laws, but new proposals could stop abortion for foetal defects.",
        ],
        [
            "Egyptian security forces target rare anti-government protests",
            "Amnesty International says two killed in unrest over law demanding residents pay fines to legalise homesRights groups say two Egyptians have been killed and hundreds more detained in a recent wave of protests, as the population continues to be hit by the econ…",
        ],
        [
            "Amnesty International Halts Work In India",
            "Amnesty International said it would cease operations in India following years of harassment and retaliation by the government, including freezing the human rights organization’s bank accounts and interrogating staff members. What do you think?Read more...",
        ],
        [
            "The Nigerian Army Reportedly Opened Fire on Peaceful Protesters. Here’s What to Know",
            "On Tuesday evening, reports and videos on social media appeared to show the Nigerian army opening fire on unarmed peaceful #endSARS protesters at the Lekki toll gate in Lagos after reportedly turning off the street lights and cutting phone networks. Casualty …",
        ],
        [
            "Palantir Admits to Helping ICE Deport Immigrants",
            "In a letter to Amnesty International meant to dismiss accusations of helping ICE deport migrants, Palantir accidentally admitted to doing so.",
        ],
        [
            "Trump administration 'acted with complete disregard' for international law by deporting Hondurans — in Guatemala — civil society groups charge",
            'Civil society groups, including Amnesty International, say the act placed "the lives of women, men, and children in danger."',
        ],
        [
            "Judicial panel into shooting, police brutality convenes in Lagos - Reuters Africa",
            "The judicial panel investigating police brutality and the shooting of protesters in Lagos convened on Monday, promising neutrality and justice.",
        ],
        [
            "In Nigeria, protests, curfews lead to petrol queues - state oil firm - Reuters India",
            "Protests against police abuses in Nigeria and curfews to curb demonstrations have affected the supply of petroleum products across the country, leading to the emergence of long queues, state oil firm, NNPC said on Tuesday.",
        ],
        [
            "Nigerian police mobilize to quell worst unrest in two decades - Reuters UK",
            "Nigeria's police chief ordered the immediate mobilisation of all force resources on Saturday to control the worst street violence in two decades stemming from protests against police brutality.",
        ],
        [
            "Soccer: Nigeria's Ogu calls on players to boycott games amid unrest - Reuters UK",
            "Nigeria midfielder John Ogu has called for a boycott of their upcoming games to protest police brutality amid ongoing violence in the commercial capital Lagos.",
        ],
        [
            "Tanzania repressing opponents as election looms: Amnesty",
            "Tanzania has escalated a crackdown on political opponents by selectively applying the law to thwart their campaign efforts ahead of this month's general election, Amnesty International said Monday.",
        ],
        [
            "Factbox: Why are Nigerians protesting against police brutality? - Reuters",
            "Factbox: Why are Nigerians protesting against police brutality?\xa0\xa0Reuters",
        ],
        [
            "Factbox: Why are Nigerians protesting against police brutality? - Reuters India",
            "Nigerians protesting police brutality have hit the streets across Africa's most populous nation for more than a week, and the hashtag #EndSARS trended on Twitter even after the police promised to dismantle the controversial unit on Oct. 11. What is SARS, what…",
        ],
    ],
    "Food-Bank-For-New-York-City": [
        [
            "At 252 tigers, Corbett's density highest worldover",
            "DEHRADUN: The fourth annual tiger estimation exercise conducted by the state forest department in association with the World Wide Fund for Nature (WWF.",
        ],
        [
            "UK brands act to cut catch of 'near-threatened' yellowfin tuna",
            "Voluntary action of companies including Tesco and Princes aims to put pressure on regulatory body to tackle overfishingBritish supermarkets and brands, including Tesco, the Co-op and Princes, are stepping up action to cut yellowfin tuna catches in the Indian …",
        ],
        [
            "Setting Science-Based Targets For Financial Institutions",
            "Over the past 2 years, SBTi of CDP, the United Nations Global Compact, the World Resources Institute, and the World Wide Fund for Nature have been developing this framework with Guidehouse.",
        ],
        [
            "Natural Disasters May Push Global Finances to the Brink",
            "In the past 20 years, 20 climate-fueled disasters have caused damage to countries worth more than 10 percent of their GDP\n\n-- Read more on ScientificAmerican.com",
        ],
        [
            "Le WWF veut «\xa0faire reculer la vente des SUV\xa0»",
            "Le\xa0World Wide Fund For Nature France (WWF France) vient de publier deux études qui fustigent les SUV à la fois pour leur consommation, mais aussi pour leur prix. La première des deux études publiées est intitulée «\xa0L’impact écrasant des SUV sur le climat\xa0». I…",
        ],
        [
            "Plástico: quimera enzimática pode ser a resposta para a reciclagem",
            "Em 2018, cientistas dos dois lados do Atlântico reprojetaram uma enzima para que ela se alimentasse mais rapidamente de plástico. Agora, a mesma equipe combinou a PETase com a MHETase para acelerar ainda mais o processo de decomposição do termoplástico tereft…",
        ],
        [
            "Space to help build a green post-pandemic economy",
            "ESA has several green initiatives to foster economic recovery from the coronavirus pandemic while promoting clean living and digital transformation. They seek to use disruptive technologies to transform urban green areas, improve air quality and offer space-b…",
        ],
        [
            "Indian Embassy in Madagascar to go solar on October 2",
            "It will be the first Indian mission globally to become clean and green with this installation.",
        ],
        [
            "ASSA ABLOY commits to science-based sustainability targets",
            "ASSA ABLOY, the global leader in access solutions, is committing to science-based targets to further substantially reduce its greenhouse gas emissions across the entire value chain. The Group will set targets that are aligned to the Paris Agreement, limiting …",
        ],
        [
            "The Chinchillas And The Gold Mine",
            "In Chile, 25 rare chinchillas sit atop 3.5 million ounces of extractable gold. Can a mining company safely move them?",
        ],
        [
            "国内初！寄付先が選べるペットボトル回収機ビオセボン２店舗（麻布十番店・武蔵小杉店）に設置",
            "[イオン株式会社]\n■ペットボトル回収機について\n\n[画像1: https://prtimes.jp/i/7505/2327/resize/d7505-2327-569843-0.jpg ]\n\n▲ペットボトル回収機イメージ\n\n・空のペットボトルを１８０本収納可能（５００mlペットボトル換算）\n...",
        ],
        [
            "First koala born at Canberra zoo named after fire-ravaged national park",
            "The National Zoo and Aquarium in Canberra welcomes the first baby koala to be born at the zoo — and its name is a tribute to the ACT's beloved national park, much of which was destroyed by bushfires earlier this year.",
        ],
        [
            "EU lawmakers vote for ‘veggie burgers’ & ‘vegan sausages,’ rejecting demands by farmers",
            "Plant-based products sold in the EU should be allowed to be called ‘burgers,’ ‘sausages,’ and ‘steak,’ despite containing no meat at all, the European Parliament said. Read Full Article at RT.com",
        ],
        [
            "湄公河生態系統的衰落......",
            "內容:\xa0\r\n國際\r\n環境\r\n自由標籤:\xa0\r\n湄公河\r\n東南亞\r\n氣候變化\r\n氣候危機\r\n洞裡薩湖\r\n上圖：洞裡薩湖中被淹的森林一處。圖片來源：The Diplomat\r\n\n來源：The Diplomat 外交家作者：Tom Fawthrop日期：2020年9月2日編譯：全球化監察\r\n\n洞裡薩湖（Tonle Sap）是湄公河的「心臟」，她的萎縮，再一次敲響了河流生態系統受損的警鐘。\r\n\n東南亞人民把湄公河譽為母親河。每年雨季，河水湧入洞裡薩湖；旱季湖水再倒灌入湄公河，維持河流的生態系統。然而這種自然的自我調節功能，…",
        ],
        ["WWF sieht illegalen Tigerhandel in Europa florieren", None],
        [
            "EDP sobe fasquia na descarbonização e quer reduzir emissões em 90% face a 2015",
            "A estratégia de descarbonização da EDP está desta forma alinhada com a trajetória definida pela ciência de limitar o aumento da temperatura média global a 1,5ºC.",
        ],
        ["WWF: Mehrheit gegen weitere Skigebiete und Seilbahnen", None],
        [
            "Green tech transition needs long-term planning, not eye-catching ideas - E&T Magazine",
            "Clear understanding of the consequences of moving to sustainable technologies is needed if the billions planned to be spent on helping economies recovering from the current pandemic are to have lasting results.",
        ],
        [
            "Russia: Toxic algae blamed for death of marine life",
            "Hundreds of octopuses, seals and sea urchins washed up dead earlier this month in what was first thought to be an oil spill. Russian authorities now say a natural occurrence was responsible for the ecological disaster",
        ],
        [
            "Stoppt Essensverschwendung - Millionen Tonnen landen im Müll",
            "Auf dem Weg vom Acker oder von zum Esstisch landen in Deutschland weiterhin Jahr für Jahr viele Millionen Tonnen Lebensmittel im Müll.Foto: AFP/Getty Images",
        ],
    ],
}

populatedCharities = [
    [
        420,
        "Red Cross",
        "We're sorry if our logo gives you PTSD about math.",
        [
            [
                "Philippines' Duterte promises payment as Red Cross stops COVID-19 tests - Reuters India",
                "Philippines' Duterte promises payment as Red Cross stops COVID-19 tests\xa0\xa0Reuters India",
            ],
            [
                "Belgium needs plasma to continue COVID-19 studies, Red Cross says - Reuters India",
                "Belgium needs plasma to continue COVID-19 studies, Red Cross says\xa0\xa0Reuters India",
            ],
            [
                "Four dead, several injured in Beirut fuel tank explosion - Reuters",
                "Four people were killed and several more were wounded when a fuel tank exploded in a Beirut building on Friday, the Lebanese Red Cross said.",
            ],
            [
                "Spain's Canary Islands see new influx of African migrants",
                "More than 1,000 have arrived in recent days and this year has seen a big increase from 2019.",
            ],
            [
                "France church attacker was carrying Italian Red Cross ID - prosecutor - Reuters",
                "The man suspected of killing three people in a French church arrived by train carrying an Italian Red Cross identity document, changed his clothes at the train station, then walked to the church to begin his attack, a prosecutor said on Thursday.",
            ],
            [
                "France church attacker was carrying Italian Red Cross ID - prosecutor - Reuters UK",
                "The man suspected of killing three people in a French church arrived by train carrying an Italian Red Cross identity document, changed his clothes at the train station, then walked to the church to begin his attack, a prosecutor said on Thursday.",
            ],
            [
                "Canary Islands sees biggest migrant surge since 2006 - Reuters UK",
                "More than 1,000 migrants reached the Canary Islands in the past 48 hours, the Red Cross said on Saturday, the largest number since a 2006 crisis in the archipelago.",
            ],
            [
                "Yemen's warring parties start swap of 1,000 prisoners - Reuters Canada",
                "Planes carrying prisoners exchanged by the warring parties in Yemen took off from three airports on Thursday in an operation to return about 1,000 men home across the front lines, the International Committee of the Red Cross said.",
            ],
            [
                "Philippines' Duterte promises payment as Red Cross stops COVID-19 tests - Reuters",
                "Philippine President Rodrigo Duterte said on Friday his government will pay the 931 million pesos ($19.25 million) it owes the Red Cross after the humanitarian agency stopped conducting COVID-19 tests.",
            ],
            [
                "Red Cross says boat carrying aid attacked in Myanmar's Rakhine state - Reuters",
                "The International Committee of the Red Cross said on Wednesday a boat carrying its aid in Myanmar's restive Rakhine State had come under attack, in an incident in which the army said it was returning fire from insurgents.",
            ],
            [
                "Nigerian police pledge ICRC training as thousands protest nationwide - Reuters Canada",
                "The International Committee of the Red Cross (ICRC) will help train Nigeria's new tactical force as thousands nationwide continued to march against police brutality and in demand of further reforms, Nigeria's police inspector general said in a statement on Su…",
            ],
            [
                "Nigerian police pledge ICRC training as thousands protest nationwide - Reuters",
                "The International Committee of the Red Cross (ICRC) will help train Nigeria's new tactical force as thousands nationwide continued to march against police brutality and in demand of further reforms, Nigeria's police inspector general said in a statement on Su…",
            ],
            [
                "Red Cross urges Armenia, Azerbaijan to firm up prisoner, body swap - Reuters",
                "The International Committee of the Red Cross urged Armenia and Azerbaijan on Tuesday to finalize arrangements for it to handle an exchange of detainees and bodies from the Nagorno-Karabakh conflict, after a humanitarian ceasefire agreed at the weekend.",
            ],
            [
                "Yemen's largest prisoner swap to go ahead on Thursday - ICRC - Reuters.com",
                "Planes carrying prisoners exchanged by the warring parties in Yemen are set to take off on Thursday in an operation to return about 1,000 men home across the front lines, the International Committee of the Red Cross (ICRC) said.",
            ],
            [
                "Yemen's largest prisoner swap to go ahead on Thursday: ICRC - Reuters",
                "Planes carrying prisoners exchanged by the warring parties in Yemen are set to take off on Thursday in an operation to return about 1,000 men home across the front lines, the International Committee of the Red Cross (ICRC) said.",
            ],
            [
                "Belgium needs plasma to continue COVID-19 studies, Red Cross says - Reuters",
                "Belgian clinical studies to study the effectiveness of blood plasma for people recovering from COVID-19 are at risk of being suspended because of low plasma stocks, doctors said, prompting a call for more blood donors to come forward.",
            ],
            [
                "Vietnam faces deadly flooding disaster - Red Cross",
                "Floodwaters have killed over 100 and left homes submerged, crops destroyed and livestock swept away.",
            ],
            [
                "Typhoon Molave: Landslides kill at least 19 after heavy rain in Vietnam",
                "Dozens are still missing after Typhoon Molave struck central Vietnam, lashing it with wind and rain.",
            ],
            [
                "Channeling 'anger into art', artists in Beirut process blast - Reuters UK",
                "Channeling 'anger into art', artists in Beirut process blast\xa0\xa0Reuters UK",
            ],
            [
                "Canary Islands sees biggest migrant surge since 2006 - Reuters",
                "Canary Islands sees biggest migrant surge since 2006\xa0\xa0Reuters",
            ],
        ],
        "420.png",
    ],
    [
        421,
        "Humane Society",
        "It's <i>humane</i> not human.",
        [
            [
                "Skateboarding TikTok Star Nathan Apodaca Gets Another Big Break - HuffPost Canada",
                "<ol><li>Skateboarding TikTok Star Nathan Apodaca Gets Another Big Break\xa0\xa0HuffPost Canada\r\n</li><li>Courteney Cox Recreates Viral 'Dreams' TikTok With Roller Skates & Cranberry Juice\xa0\xa0Access Hollywood\r\n</li><li>The Best Canadian Versions of the “Dreams” TikTok…",
            ],
            [
                "Hand over the trash: raccoons break into California bank",
                "Pair were noticed causing havoc inside bank by customer withdrawing money outside the buildingTwo “masked” intruders broke into a California bank using a method straight out of the movies: crawling along air ducts – only to fall through the ceiling tiles and …",
            ],
            [
                "Masked Intruders Break Into Bank",
                "An ATM user outside a Redwood City, California, bank noticed that there were things going on inside the closed lobby. Two young raccoons were trapped inside, apparently after climbing through the air ducts to get into the bank. Bank managers and staff from th…",
            ],
            [
                "‘It’s important for the political world of today to own up to their mistakes in public’",
                "Carnatic classical vocalist TM Krishna’s 'The Edict Project' will musically attempt to rediscover King Ashoka’s famed edicts -- philosophies that speak of a more humane society built on empathy and compassion",
            ],
            [
                "'The cougar guy': Utah hiker encounters a cougar who followed him for nearly six minutes",
                "Kyle Burgess of Orem, Utah, stopped to record cubs he saw during his evening run. He was soon being followed by a mother cougar for nearly six minutes.",
            ],
            [
                "Farewell, Fido: U.S. cities see boom in pet cemeteries - Reuters.com",
                "When Jim LaMar's border collie, KC, died in 2012, he had her cremated and kept the remains with him in his California home.",
            ],
            [
                "Elderly shelter pets getting adopted in the coolest way (34 Photos)",
                "The Flagler Humane Society did a photoshoot with their elderly cats and dogs in order to help them get adopted",
            ],
            [
                "Animal Humane Society CEO Janelle Dixon garners 2020 Women in Business award - Minneapolis / St. Paul Business Journal",
                "Animal Humane Society CEO Janelle Dixon garners 2020 Women in Business award\xa0\xa0Minneapolis / St. Paul Business Journal",
            ],
            [
                "TX Family's Dog Stolen 6 Years Ago -- Found In Florida...",
                "TX Family's Dog Stolen 6 Years Ago -- Found In Florida...\r\n\n \n \n \n (Third column, 15th story, link)",
            ],
            [
                "2021 Pooping Dogs Calendar Is Here, and This Year Contains a Puzzle",
                "White Elephant Party coming up? Yankee Swap? Secret Santa? Do you know someone who loves dogs...too much? This 12 month calendar of pooping dogs will be the most memorable gift you give this year. \r\n\r\nTalk about a gift that keeps on giving; each month reveals…",
            ],
            [
                "Raccoons break into bank...",
                'Two young raccoons were caught "breaking into" a California bank, living up to their masked bandit reputation.',
            ],
            [
                "Nordstrom to end the sale of fur and animal skins",
                "One of America's leading fashion retailers, Nordstrom, has announced that it will be ending the sale of fur and animal skins by 2021. This move comes at a time when the world is faced with various environmental issues that are forcing many people to rethink t…",
            ],
            [
                "Nordstrom to stop selling fur and exotic animal skins by the end of 2021",
                "<p>Humane Society hopes move will have a ripple effect on other fashion leaders</p>",
            ],
            [
                "Nordstrom to stop selling fur, exotic animal skin products",
                "Upscale retailer is first in the nation to ban skins from kangaroos, snakes and alligators, Humane Society says.",
            ],
            [
                "'Real and imminent' extinction risk to whales",
                "A letter signed by hundreds of scientists calls for global action to protect whales, dolphins and porpoises.",
            ],
            [
                "'Real and imminent' extinction risk to whales",
                "A letter signed by hundreds of scientists calls for global action to protect whales, dolphins and porpoises.",
            ],
            [
                "'Sheer anxiety': Louisiana braces itself for Hurricane Delta",
                "Louisiana residents still recovering from the devastation of a powerful hurricane less than two months ago braced for another hit as Hurricane Delta steamed north through the Gulf on Thursday after swiping Mexico's Yucatan Peninsula.",
            ],
            [
                "Nordstrom Will No Longer Sell Fur and Exotic-Animal Skins",
                "It’s the first U.S. retailer to ban the latter.",
            ],
            [
                "U.S. Lab Chimps Stuck in Retirement Limbo",
                "Activists and some congressional lawmakers are demanding that the N.I.H. reconsider its refusal to move 39 chimpanzees from a research center to a sanctuary.",
            ],
            [
                "Doc Antle of ‘Tiger King’ Is Charged With Wildlife Trafficking",
                "Mr. Antle’s daughters and a former roadside zoo owner in Virginia also face charges of animal cruelty.",
            ],
        ],
        "421.png",
    ],
    [
        422,
        "World Wildlife Fund",
        "Our logo says <b>WWF</b> not WTF.",
        [
            [
                "At 252 tigers, Corbett's density highest worldover",
                "DEHRADUN: The fourth annual tiger estimation exercise conducted by the state forest department in association with the World Wide Fund for Nature (WWF.",
            ],
            [
                "UK brands act to cut catch of 'near-threatened' yellowfin tuna",
                "Voluntary action of companies including Tesco and Princes aims to put pressure on regulatory body to tackle overfishingBritish supermarkets and brands, including Tesco, the Co-op and Princes, are stepping up action to cut yellowfin tuna catches in the Indian …",
            ],
            [
                "Setting Science-Based Targets For Financial Institutions",
                "Over the past 2 years, SBTi of CDP, the United Nations Global Compact, the World Resources Institute, and the World Wide Fund for Nature have been developing this framework with Guidehouse.",
            ],
            [
                "Natural Disasters May Push Global Finances to the Brink",
                "In the past 20 years, 20 climate-fueled disasters have caused damage to countries worth more than 10 percent of their GDP\n\n-- Read more on ScientificAmerican.com",
            ],
            [
                "Le WWF veut «\xa0faire reculer la vente des SUV\xa0»",
                "Le\xa0World Wide Fund For Nature France (WWF France) vient de publier deux études qui fustigent les SUV à la fois pour leur consommation, mais aussi pour leur prix. La première des deux études publiées est intitulée «\xa0L’impact écrasant des SUV sur le climat\xa0». I…",
            ],
            [
                "Plástico: quimera enzimática pode ser a resposta para a reciclagem",
                "Em 2018, cientistas dos dois lados do Atlântico reprojetaram uma enzima para que ela se alimentasse mais rapidamente de plástico. Agora, a mesma equipe combinou a PETase com a MHETase para acelerar ainda mais o processo de decomposição do termoplástico tereft…",
            ],
            [
                "Space to help build a green post-pandemic economy",
                "ESA has several green initiatives to foster economic recovery from the coronavirus pandemic while promoting clean living and digital transformation. They seek to use disruptive technologies to transform urban green areas, improve air quality and offer space-b…",
            ],
            [
                "Indian Embassy in Madagascar to go solar on October 2",
                "It will be the first Indian mission globally to become clean and green with this installation.",
            ],
            [
                "ASSA ABLOY commits to science-based sustainability targets",
                "ASSA ABLOY, the global leader in access solutions, is committing to science-based targets to further substantially reduce its greenhouse gas emissions across the entire value chain. The Group will set targets that are aligned to the Paris Agreement, limiting …",
            ],
            [
                "The Chinchillas And The Gold Mine",
                "In Chile, 25 rare chinchillas sit atop 3.5 million ounces of extractable gold. Can a mining company safely move them?",
            ],
            [
                "国内初！寄付先が選べるペットボトル回収機ビオセボン２店舗（麻布十番店・武蔵小杉店）に設置",
                "[イオン株式会社]\n■ペットボトル回収機について\n\n[画像1: https://prtimes.jp/i/7505/2327/resize/d7505-2327-569843-0.jpg ]\n\n▲ペットボトル回収機イメージ\n\n・空のペットボトルを１８０本収納可能（５００mlペットボトル換算）\n...",
            ],
            [
                "First koala born at Canberra zoo named after fire-ravaged national park",
                "The National Zoo and Aquarium in Canberra welcomes the first baby koala to be born at the zoo — and its name is a tribute to the ACT's beloved national park, much of which was destroyed by bushfires earlier this year.",
            ],
            [
                "EU lawmakers vote for ‘veggie burgers’ & ‘vegan sausages,’ rejecting demands by farmers",
                "Plant-based products sold in the EU should be allowed to be called ‘burgers,’ ‘sausages,’ and ‘steak,’ despite containing no meat at all, the European Parliament said. Read Full Article at RT.com",
            ],
            [
                "湄公河生態系統的衰落......",
                "內容:\xa0\r\n國際\r\n環境\r\n自由標籤:\xa0\r\n湄公河\r\n東南亞\r\n氣候變化\r\n氣候危機\r\n洞裡薩湖\r\n上圖：洞裡薩湖中被淹的森林一處。圖片來源：The Diplomat\r\n\n來源：The Diplomat 外交家作者：Tom Fawthrop日期：2020年9月2日編譯：全球化監察\r\n\n洞裡薩湖（Tonle Sap）是湄公河的「心臟」，她的萎縮，再一次敲響了河流生態系統受損的警鐘。\r\n\n東南亞人民把湄公河譽為母親河。每年雨季，河水湧入洞裡薩湖；旱季湖水再倒灌入湄公河，維持河流的生態系統。然而這種自然的自我調節功能，…",
            ],
            ["WWF sieht illegalen Tigerhandel in Europa florieren", None],
            [
                "EDP sobe fasquia na descarbonização e quer reduzir emissões em 90% face a 2015",
                "A estratégia de descarbonização da EDP está desta forma alinhada com a trajetória definida pela ciência de limitar o aumento da temperatura média global a 1,5ºC.",
            ],
            ["WWF: Mehrheit gegen weitere Skigebiete und Seilbahnen", None],
            [
                "Green tech transition needs long-term planning, not eye-catching ideas - E&T Magazine",
                "Clear understanding of the consequences of moving to sustainable technologies is needed if the billions planned to be spent on helping economies recovering from the current pandemic are to have lasting results.",
            ],
            [
                "Russia: Toxic algae blamed for death of marine life",
                "Hundreds of octopuses, seals and sea urchins washed up dead earlier this month in what was first thought to be an oil spill. Russian authorities now say a natural occurrence was responsible for the ecological disaster",
            ],
            [
                "Stoppt Essensverschwendung - Millionen Tonnen landen im Müll",
                "Auf dem Weg vom Acker oder von zum Esstisch landen in Deutschland weiterhin Jahr für Jahr viele Millionen Tonnen Lebensmittel im Müll.Foto: AFP/Getty Images",
            ],
        ],
        "422.png",
    ],
    [
        423,
        "UNICEF",
        "Treat or treat for UNICEF (if you know, you know)",
        [
            [
                "UNICEF Plans to Stockpile Syringes in Preparation for First Vaccines",
                "The U.N. agency said it was amassing medical equipment to be ready when the time comes. Total global virus cases surpassed 40 million. Here’s the latest.",
            ],
            [
                "U.N.'s IOM and UNICEF vow to investigate 'jobs-for-sex' claims in Congo - Reuters India",
                "Two more U.N. agencies joined the World Health Organization (WHO) with pledges on Wednesday to investigate claims of sexual exploitation by aid workers in the Democratic Republic of Congo uncovered by the Thomson Reuters Foundation and The New Humanitarian.",
            ],
            [
                "U.N.'s IOM and UNICEF vow to investigate 'jobs-for-sex' claims in Congo - Reuters",
                "Two more U.N. agencies joined the World Health Organization (WHO) with pledges on Wednesday to investigate claims of sexual exploitation by aid workers in the Democratic Republic of Congo uncovered by the Thomson Reuters Foundation and The New Humanitarian.",
            ],
            [
                "Moncler pledges carbon neutrality by 2021, recycling in new plan - Reuters",
                "Luxury puffer jacket maker Moncler <MONC.MI> committed on Thursday to making production sites carbon-neutral by 2021 and said it would start using from January certified recycled down, in a process requiring 70% less water than the traditional one.",
            ],
            [
                "NZ election: The people left behind in Ardern's 'kind' New Zealand",
                "Critics say Jacinda Ardern has not done enough to combat child poverty as she seeks another term.",
            ],
            [
                "New mom Katy Perry checks out $4M Santa Barbara beach home as she seeks nest for 1-month-old daughter Daisy - The Sun",
                "<ol><li>New mom Katy Perry checks out $4M Santa Barbara beach home as she seeks nest for 1-month-old daughter Daisy\xa0\xa0The Sun\r\n</li><li>Jane Fonda leads celebrity workout class to encourage voting\xa0\xa0The Independent\r\n</li><li>Jane Fonda back to her eighties work…",
            ],
            [
                "Muere Quino, el creador de Mafalda, a los 88 años",
                "Ha muerto Joaquín Salvador Lavado Tejó, mejor conocido como Quino, creador de Mafalda y uno de los artistas más reconocidos de Argentina. La noticia fue confirmada por su editor, Daniel Davisnky en redes sociales. Según informaciones publicadas por medios loc…",
            ],
            [
                "The Campaign To Wipe Out Polio Was Going Really Well ... Until It Wasn't",
                'It looked as if polio would be the second human disease to be eliminated — after smallpox. But "2020 has been a terrible year," says Michel Zaffran, head of the Global Polio Eradication Initiative.',
            ],
            [
                "Kurdish official says thousands of Syrians to leave crowded camp in northeast - Reuters",
                "Kurdish-led authorities said on Monday up to 15,000 Syrians could be moved out of the overcrowded al-Hol camp in northeast Syria which holds displaced people and families of Islamic State fighters.",
            ],
            [
                "Congo to investigate 'jobs-for-sex' accusations during Ebola outbreak - Reuters",
                "Congo to investigate 'jobs-for-sex' accusations during Ebola outbreak\xa0\xa0Reuters",
            ],
            [
                "Jamaican teacher turns Kingston walls into blackboards - Reuters UK",
                "With most schools in Jamaica still closed due to the pandemic, schoolteacher Taneka Mckoy every day braves the risk of stray gunshots from gang warfare and the oppressive Caribbean heat as she trudges around her inner city Kingston community to write lessons …",
            ],
            [
                "Kenya partially reopens schools, six months after COVID closed them - Reuters India",
                "Kenyan schoolchildren in grades four, eight and 12 returned to class on Monday, ending a months-long closure of all educational institutions in the country designed to slow the spread of the novel coronavirus.",
            ],
            [
                "Kurdish official says thousands of Syrians to leave crowded camp in northeast - Reuters UK",
                "Kurdish-led authorities said on Monday up to 15,000 Syrians could be moved out of the overcrowded al-Hol camp in northeast Syria which holds displaced people and families of Islamic State fighters.",
            ],
            [
                "UK bans sex between government aid workers and recipients to rein in abuse - Reuters",
                "Britain has banned sexual relations between government staff giving aid and people receiving it, as lawmakers seek to stamp out abuse in the aid sector following a string of sex scandals.",
            ],
            [
                "Kenya partially reopens schools, six months after COVID closed them - Reuters India",
                "Kenyan schoolchildren in grades four, eight and 12 returned to class on Monday, ending a months-long closure of all educational institutions in the country designed to slow the spread of the novel coronavirus.",
            ],
            [
                "Overstretched health visitors caring for up to 2,400 families each",
                "Exclusive: concerns for mental health and breastfeeding rates owing to already overstretched service in England<ul><li>Alone and in pain: one woman’s struggle for support</li></ul>Overstretched health visitors have been forced to care for up to 2,400 families…",
            ],
            [
                "Facebook bans ads that discourage people from getting vaccines",
                "Facebook will start banning ads that explicitly discourage people from getting vaccinated, the world's largest social media company said on Tuesday.",
            ],
            [
                "COVID-19 Has Robbed The World's Poorest Children Of Nearly 4 Months Of Schooling",
                "A new report finds the return to education has been much slower in the world's poorer countries.",
            ],
            [
                "Facebook is finally banning anti-vax ads from its platform and Instagram",
                "Anti-vaxxers must be steaming. In an effort to curb health misinformation amidst the coronavirus pandemic, Facebook has revealed it’ll start purging ads that discourage vaccines and immunization on its platform and Instagram. As the Wall Street Journal notes,…",
            ],
            [
                "Kinderhilfswerk: Corona: Unicef lagert 520 Millionen Spritzen für Impfung ein",
                "",
            ],
        ],
        "423.png",
    ],
    [
        424,
        "Amnesty International",
        "<i>We can't expect God to do all the work</i> -Joshua Graham (<i>Fallout: New Vegas</i>)",
        [
            [
                "Prison set on fire in Nigeria as protest death toll rises to at least 56",
                "At least 56 people have died across Nigeria since the #EndSARS protests began on October 8, with 38 killed across the country on Tuesday alone, according to human rights group Amnesty International.",
            ],
            [
                "Political failings put Colombian activists at risk: Amnesty - Reuters",
                "Frequent threats, attacks and killings targeting local activists across Colombia highlight the government's inability to protect human rights defenders, advocacy group Amnesty International said on Thursday.",
            ],
            [
                "Non-profits say India's new rules on foreign funding will hit operations - Reuters",
                "India's tougher rules on foreign funding for non-profits will severely crimp their activities, the chiefs of some bodies said on Thursday, after human rights group Amnesty International suspended its work in the country, citing government harassment.",
            ],
            [
                "Amnesty disputes Nigerian army claim it did not shoot Lagos civilians - Reuters India",
                "Nigeria's Lagos state government asked the army to intervene to restore order amid anti-police brutality protests, but soldiers did not shoot civilians, the military said, an assertion an Amnesty International investigation disputed on Wednesday.",
            ],
            [
                "What's Happening in Nigeria?",
                "After a summer of ongoing protests over police violence—including the murders of George Floyd and Breonna Taylor—greater numbers of Americans are starting to understand this facet of systemic racism. Of course, it’s not only an issue in the United States, and…",
            ],
            [
                "Afghan-Taliban conflict: Fears grow for families trapped in Helmand",
                "Aid groups say civilians must be given safe passage amid clashes between Taliban and government forces.",
            ],
            [
                "Nigerian president criticised over response to protests crackdown",
                "Muhammadu Buhari urged to address nation after shootings by security forces on Tuesday Nigeria’s president, Muhammadu Buhari, has been criticised for his muted response after security forces opened fire on people protesting against police brutality in Lagos o…",
            ],
            [
                "Poland abortion: Top court to rule on almost total ban",
                "Poland has some of Europe's strictest laws, but new proposals could stop abortion for foetal defects.",
            ],
            [
                "Egyptian security forces target rare anti-government protests",
                "Amnesty International says two killed in unrest over law demanding residents pay fines to legalise homesRights groups say two Egyptians have been killed and hundreds more detained in a recent wave of protests, as the population continues to be hit by the econ…",
            ],
            [
                "Amnesty International Halts Work In India",
                "Amnesty International said it would cease operations in India following years of harassment and retaliation by the government, including freezing the human rights organization’s bank accounts and interrogating staff members. What do you think?Read more...",
            ],
            [
                "The Nigerian Army Reportedly Opened Fire on Peaceful Protesters. Here’s What to Know",
                "On Tuesday evening, reports and videos on social media appeared to show the Nigerian army opening fire on unarmed peaceful #endSARS protesters at the Lekki toll gate in Lagos after reportedly turning off the street lights and cutting phone networks. Casualty …",
            ],
            [
                "Palantir Admits to Helping ICE Deport Immigrants",
                "In a letter to Amnesty International meant to dismiss accusations of helping ICE deport migrants, Palantir accidentally admitted to doing so.",
            ],
            [
                "Trump administration 'acted with complete disregard' for international law by deporting Hondurans — in Guatemala — civil society groups charge",
                'Civil society groups, including Amnesty International, say the act placed "the lives of women, men, and children in danger."',
            ],
            [
                "Judicial panel into shooting, police brutality convenes in Lagos - Reuters Africa",
                "The judicial panel investigating police brutality and the shooting of protesters in Lagos convened on Monday, promising neutrality and justice.",
            ],
            [
                "In Nigeria, protests, curfews lead to petrol queues - state oil firm - Reuters India",
                "Protests against police abuses in Nigeria and curfews to curb demonstrations have affected the supply of petroleum products across the country, leading to the emergence of long queues, state oil firm, NNPC said on Tuesday.",
            ],
            [
                "Nigerian police mobilize to quell worst unrest in two decades - Reuters UK",
                "Nigeria's police chief ordered the immediate mobilisation of all force resources on Saturday to control the worst street violence in two decades stemming from protests against police brutality.",
            ],
            [
                "Soccer: Nigeria's Ogu calls on players to boycott games amid unrest - Reuters UK",
                "Nigeria midfielder John Ogu has called for a boycott of their upcoming games to protest police brutality amid ongoing violence in the commercial capital Lagos.",
            ],
            [
                "Tanzania repressing opponents as election looms: Amnesty",
                "Tanzania has escalated a crackdown on political opponents by selectively applying the law to thwart their campaign efforts ahead of this month's general election, Amnesty International said Monday.",
            ],
            [
                "Factbox: Why are Nigerians protesting against police brutality? - Reuters",
                "Factbox: Why are Nigerians protesting against police brutality?\xa0\xa0Reuters",
            ],
            [
                "Factbox: Why are Nigerians protesting against police brutality? - Reuters India",
                "Nigerians protesting police brutality have hit the streets across Africa's most populous nation for more than a week, and the hashtag #EndSARS trended on Twitter even after the police promised to dismantle the controversial unit on Oct. 11. What is SARS, what…",
            ],
        ],
        "424.png",
    ],
]
