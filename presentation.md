# Presentation Script — Roman Urdu
## "Fantastic Joules and Where to Find Them"
### IMC '25 Paper Reproduction — Final Presentation

---

> **Kirdar (Roles):**
> - **Ahmad** → Presenter & Storyteller (main bolta hai, narrative chalata hai)
> - **Umair Hafeez** → Environment & Setup Expert (slides dikhata hai, terminal dikhata hai)
> - **M. Umair** → Results Analyst (figures aur tables dikhata hai, numbers explain karta hai)

---

---

# SLIDE 1 — Title Slide

**[Umair Hafeez screen pe title slide lagata hai]**

**Ahmad bolta hai:**

> "Assalam o Alaikum. Mera naam Ahmad hai, aur mere saath hain Umair Hafeez aur M. Umair. Aaj hum aapke saamne ek research paper ki reproduction present karenge jiska naam hai — *Fantastic Joules and Where to Find Them.* Yeh paper IMC 2025 mein publish hua, jo duniya ki top networking research conferences mein se ek hai. Toh chalein shuru karte hain."

---

# SLIDE 2 — Ek Sawal Se Shuruat

**[Slide: Sirf ek bada sawal — "Internet kitni bijli khaata hai?"]**

**Ahmad bolta hai:**

> "Socho — abhi is waqt duniya mein hazaron routers chal rahe hain. Har router bijli khaata hai. Lekin kisi ko pata nahi — exactly kitni? Datasheet mein jo likha hai woh sach hai? PSU jo measure karta hai woh accurate hai? Aur kya hum pehle se predict kar sakte hain ke ek router kitna power draw karega?
>
> Yeh teen simple lagte sawaal hain. Lekin is paper ke researchers ne discover kiya ke inke jawab bohot mushkil hain — aur kabhi kabhi bilkul ghalat bhi. Yahi is paper ki kahani hai."

---

# SLIDE 3 — Paper Ka Background

**[Slide: ICT sector = 4% global electricity, Internet = 1-1.5%]**

**Ahmad bolta hai:**

> "2020 ki report ke mutabiq, Information and Communication Technology sector global electricity ka 4% consume karta hai. Iss mein se Internet ka hissa 1 se 1.5 percent hai. Aur yeh continuously badh raha hai.
>
> Ab sochein — agar hum Internet ki energy kam karna chahein, toh sabse pehle yeh samajhna hoga ke energy jaati kahan hai. Aur researchers ne discover kiya ke routers — yani woh hardware jo Internet ka backbone hai — unke baare mein hamen kuch pata hi nahi.
>
> Isliye yeh paper likha gaya."

---

# SLIDE 4 — Yeh Paper Kis Liye Hai?

**[Slide: Teen Research Questions — Q1, Q2, Q3]**

**Ahmad bolta hai:**

> "Is paper mein researchers ne teen core sawaal pooche:
>
> **Q1:** Kya router ki datasheet — yani manufacturer ka document — actual power draw ka sahi andaza lagaati hai?
>
> **Q2:** Kya router ke andar jo PSU, yani Power Supply Unit, power measure karta hai — kya woh measurements trustworthy hain?
>
> **Q3:** Kya hum ek mathematical model se accurately predict kar sakte hain ke ek router kitna power khaayega?
>
> Yeh teen sawaal simple lagte hain — lekin inke jawab chahiye the ek unique dataset, real ISP network access, aur physical router measurements. Toh researchers ne yahi kiya."

---

# SLIDE 5 — Dataset Ka Taaruf

**[Slide: Dataset overview — 4 types of data]**

**Ahmad bolta hai:**

> "Researchers ne ek bohot special dataset banaya. Iss dataset mein char cheezein hain:
>
> Pehli — 777 router models ke datasheets ka collection, Cisco, Juniper aur Arista se.
>
> Doosri — Switch naam ki ek Swiss ISP hai — Tier-2 level — unke 107 routers ka 10 mahine ka power data, SNMP ke zariye.
>
> Teesri — Unhi routers ka 2 mahine ka external power measurement — ek custom hardware system se jiska naam hai Autopower.
>
> Aur chauthi — 8 router models ke fine-grained power models, lab experiments se.
>
> Yeh dataset duniya mein aisa pehla publicly available dataset hai jo itna detailed router power data provide karta hai."

---

# SLIDE 6 — Humara Kaam — Reproduction

**[Slide: Humara scope — kya reproduce kiya]**

**Ahmad bolta hai:**

> "Humara kaam tha is paper ke results ko reproduce karna — yani same code chalana, same data use karna, aur check karna ke kya wahi numbers aate hain jo paper mein hain.
>
> Humne do notebooks run kiye — datasheet-analysis aur PSU-efficiency-analysis. Aur humne cover kiye:
> Section 3 ke results — Table 1 aur Figures 2a, 2b
> Section 7 ke results — traffic energy cost
> Section 9 ke results — Table 3 aur Table 4, aur Figures 5 aur 6
>
> Ab main apne saathiyon ko invite karta hoon — pehle Umair Hafeez batayenge ke humne environment kaise set kiya — aur kya mushkilat aayi."

---

# SLIDE 7 — Environment Setup

**[Umair Hafeez aage aata hai. Screen pe VS Code aur terminal dikhata hai.]**

**Umair Hafeez bolta hai:**

> "Thank you Ahmad. Main Umair Hafeez hoon aur maine is project ka poora technical setup kiya.
>
> Sabse pehle humne GitHub se project clone kiya aur Python virtual environment banaya. Phir requirements install karne ki koshish ki. Lekin yahan se mushkilat shuru hui.
>
> **Pehli mushkil:** requirements.txt mein `numpy` aur `scipy` listed hi nahi the. Lekin notebooks mein dono use ho rahe the — numpy math operations ke liye aur scipy PSU load calculation ke liye. Humne manually discover kiya aur requirements mein add kiye.
>
> **Doosri mushkil — yeh zyada serious thi:** Plotly ki version 5.21.0 pinned thi requirements mein, lekin jab hum `pip install kaleido` karte hain toh kaleido 1.3.0 install hoti hai — jo plotly 6.1 maangta hai. Toh `fig.write_image()` fail ho jata tha is error ke saath:"

**[Screen pe error dikhata hai:]**
```
ValueError: Image export using the "kaleido" engine requires the kaleido package...
```

**Umair Hafeez continue karta hai:**

> "Humne solution nikala — kaleido ko version 0.2.1 pe downgrade kiya jo plotly 5.21 ke saath compatible hai. Aur requirements.txt update kiya taake future mein kisi ko yeh issue na aaye.
>
> **Teesri cheez:** Jupyter kernel ko restart karna pada kyunki purani kaleido memory mein cached thi.
>
> **Chauthi cheez:** VS Code galat Python interpreter use kar raha tha — system ka Python, venv ka nahi. Isliye editor mein warnings aa rahi thin. Humne interpreter switch kiya venv ke python.exe pe.
>
> Yeh saari cheezein paper ke original README mein document nahi thin. Humne in sab ko discover kiya, fix kiya, aur requirements.txt update kiya. Ab main M. Umair ko deta hoon jo results explain karega."

---

# SLIDE 8 — Section 3: Datasheet Analysis

**[M. Umair aage aata hai. Screen pe Figure 2 aur Table 1 dikhata hai.]**

**M. Umair bolta hai:**

> "Shukriya Umair Hafeez. Main M. Umair hoon aur maine results ka paper ke saath comparison kiya.
>
> Shuru karte hain Section 3 se — Datasheet Analysis.
>
> Researchers ka pehla sawaal tha: Kya datasheets accurate hain? Toh unhone 777 routers ke datasheets collect kiye aur unka actual measured power se compare kiya.
>
> Yeh dekhiye — Table 1."

**[Screen pe Table 1 dikhata hai — reproduced version]**

**M. Umair continue karta hai:**

> "Hamare results ekdum paper ke saath match karte hain. Har ek number same hai.
>
> Dekhiye — NCS-55A1-24H router: datasheet kehta hai 600 Watt. Actual measured tha 358 Watt. Matlab datasheet ne 40% overestimate kiya. Yeh to theek hai — datasheets usually overestimate karte hain safety margin ke liye.
>
> Lekin yeh dekho — 8201-32FH: datasheet kehta hai 288 Watt, actual measurement hai 359 Watt. Yani datasheet ne *underestimate* kiya — minus 24 percent! Aur 8201-24H8FH mein toh minus 44 percent!
>
> Matlab kuch routers actually apni datasheet se zyada bijli kha rahe hain — aur yeh ISP operators ke liye ek serious problem hai kyunki woh power planning datasheets pe karte hain."

---

# SLIDE 9 — Section 3: Efficiency Trends

**[Screen pe Figure 2a aur 2b dikhata hai — side by side]**

**M. Umair bolta hai:**

> "Ab yeh do graphs dekho.
>
> Baayein taraf — Figure 2a — Broadcom ke ASIC chips ki efficiency. 2010 se 2022 tak, efficiency clearly improve hui hai — 25 Watt per 100 Gbps se ghar ke 1 Watt tak. Ek clear downward trend hai.
>
> Daayein taraf — Figure 2b — Hamare reproduced datasheet scatter plot. Yahi cheez router level pe dekhte hain. Koi trend nahi hai. Points scattered hain. Koi improvement visible nahi.
>
> Matlab individual components behtar hote ja rahe hain — lekin pura router system as a whole mein yeh improvement nazar nahi aati. Yeh ek important finding hai."

---

# SLIDE 10 — Section 7: Traffic Ka Power Pe Asar

**[Screen pe Figure 1 — total power aur traffic time series]**

**M. Umair bolta hai:**

> "Ab Figure 1 dekhte hain — Switch ISP ke poore network ka power aur traffic September se November 2024 tak.
>
> Upper line hai total power — roughly 21,500 se 22,000 Watt ke beech. Bohot flat hai.
>
> Neeli line hai total traffic — yeh upar neeche jaati rehti hai.
>
> Yeh graph ek zarori baat prove karta hai: traffic aur power mein koi direct correlation nahi hai. Jab traffic double ho, power same rahta hai. Yeh counter-intuitive hai — lekin yahi sach hai.
>
> Numbers bhi hain: 100 Gbps traffic forward karne ka cost sirf 0.62 Watt hai 1500 byte packets ke liye, aur 3.43 Watt hai 64 byte packets ke liye. Poore Switch network ka total traffic cost sirf 5.81 Watt — yani total network power ka 0.026 percent. Negligible.
>
> Isliye researchers kehte hain: traffic kam karo ya zyada karo — router power basically same rahega."

---

# SLIDE 11 — Section 9: PSU Efficiency

**[Screen pe Figure 5 — 80 Plus curves]**

**M. Umair bolta hai:**

> "Ab section 9 — yeh is paper ka sabse interesting aur actionable hissa hai.
>
> Pehle yeh samjho ke PSU kya hota hai. Power Supply Unit router ko AC power leke DC mein convert karta hai. Lekin yeh conversion perfect nahi hoti — kuch power waste hoti hai. Yeh waste kitna hai yeh depend karta hai efficiency pe.
>
> Yeh Figure 5 hai — 80 Plus standard curves. 80 Plus ek certification hai jo PSU manufacturers ke liye hai. Bronze se shuru ho ke Titanium tak jaata hai — jitna acha standard, utni zyada efficiency.
>
> Important cheez yeh hai: PSU efficiency load pe depend karti hai. 50% load pe efficiency best hoti hai. 10-20% load pe efficiency kharaab ho jaati hai.
>
> Aur Switch network mein researchers ne find kiya ke zyada tar PSUs sirf 10 se 20 percent load pe chal rahi hain. Matlab worst efficiency range mein."

---

# SLIDE 12 — Section 9: PSU Efficiency Data

**[Screen pe Figure 6a — all PSU efficiency scatter]**

**M. Umair bolta hai:**

> "Yeh Figure 6 hai — hamare reproduced scatter plot. Har point ek PSU measurement hai.
>
> X-axis pe load percentage hai — 5 se 20 percent ke beech.
> Y-axis pe efficiency hai — 0.6 se 1.0 ke beech.
>
> Dekhiye kitna spread hai! Kuch PSUs 95 percent se upar efficient hain — kuch 60 percent se neeche. Aur yeh same router model ke PSUs hain! Matlab manufacturing quality ya aging ki wajah se itna farq hai.
>
> Yeh finding important hai: hum assume nahi kar sakte ke router PSUs efficient hain."

---

# SLIDE 13 — Table 3: Savings Estimates

**[Screen pe Table 3 — reproduced numbers]**

**M. Umair bolta hai:**

> "Ab yeh Table 3 hai — agar PSUs behtar hote toh kitni bijli bachti?
>
> Humara reproduced result paper ke saath bilkul exact match karta hai — har number, har percentage.
>
> Agar sab PSUs Bronze standard pe hon — 2 percent savings — 482 Watt.
> Agar Platinum — 5 percent — 1156 Watt.
> Agar Titanium — 7 percent — 1563 Watt.
>
> Phir researchers ne socha — kya ho agar ek router mein do PSUs hain, hum ek band kar dein aur sirf ek pe chalayen? Yeh technique hot stand-by kehlaati hai. Iss se 4 percent — 1002 Watt bachta hai.
>
> Aur agar dono combine karen — ek behtar PSU aur sirf ek use karen — toh Titanium ke saath 9 percent — 1974 Watt. Yeh considerable saving hai — aur bina koi network configuration change kiye.
>
> Yeh sab hamare numbers paper ke exact same hain. Zero discrepancy."

---

# SLIDE 14 — Table 4: Right-Sizing

**[Screen pe Table 4]**

**M. Umair bolta hai:**

> "Table 4 mein researchers ne dekha ke kya hoga agar PSU ki capacity better size ki hoti.
>
> Result yeh tha ke difference bohot chhota hai — 2 percent se minus 1 percent ke beech. Matlab PSU ki quality matters zyada — size kam matters karta hai.
>
> Yeh bhi exact match hai paper ke saath."

---

# SLIDE 15 — Kya Reproduce Nahi Hua — Aur Kyun

**[Screen pe simple bullet list]**

**Ahmad wapas aata hai:**

> "Ab ek important baat — kya nahi hua aur kyun.
>
> Figure 4 — jo Autopower hardware ka external measurement data hai — woh reproduce nahi ho saka kyunki woh data private hai. Switch ISP ne researchers ko data diya lekin public release nahi hua.
>
> Table 2 — Power models — inke liye physical router labs mein experiments chahiye the. Hum university mein hain, routers nahi hain.
>
> Section 8 — Link sleeping analysis — iske liye Switch ke private network topology ki zaroorat thi.
>
> Lekin yeh humari failure nahi hai — yeh paper ke authors ne khud likha hai Section 9.2 aur Section 11 mein ke yeh data share nahi ho sakta. Jo data publicly available tha — woh humne reproduce kar liya — aur 100% match kiya."

---

# SLIDE 16 — Summary

**[Ahmad — summary slide]**

**Ahmad bolta hai:**

> "Toh summary yeh hai:
>
> Is paper ne prove kiya ke datasheets unreliable hain — kabhi overestimate, kabhi underestimate.
>
> Prove kiya ke traffic aur power decoupled hain — bijli bachani hai toh traffic control se nahi balke hardware se sochna padega.
>
> Aur sabse actionable finding — PSU efficiency mein improvement se bina koi network change kiye 7 se 9 percent bijli bachaayi ja sakti hai.
>
> Humne yeh sab reproduce kiya — environment setup se le ke final numbers tak — aur har ek number paper se match kiya.
>
> Shukriya. Ab hum questions ke liye tayyar hain."

---

---

# Q&A SECTION — Sawaal Aur Jawab

**(Teacher ya students jo sawaal pooch sakte hain — unke complete jawab)**

---

### Q1: "Yeh paper basically kya kehna chahta hai — ek line mein?"

**Jawab (Ahmad):**
> "Yeh paper kehta hai ke hamen routers ki electricity ke baare mein jo pata tha — datasheet numbers, PSU measurements — woh ya toh ghalat hain ya unreliable hain. Aur is problem ko fix karne ke liye researchers ne ek naya dataset, naye tools, aur naya analysis provide kiya."

---

### Q2: "PSU kya hota hai aur yeh important kyun hai?"

**Jawab (M. Umair):**
> "PSU matlab Power Supply Unit. Yeh AC current ko — jo wall socket se aata hai — DC current mein convert karta hai jo router use karta hai. Yeh conversion kabhi 100% efficient nahi hoti — kuch energy heat ke roop mein waste hoti hai. Router mein usually do PSUs hote hain redundancy ke liye — agar ek fail ho toh doosra chal sake.
>
> Yeh important hai kyunki agar PSU ki efficiency kharaab hai — jaise ke 10 percent load pe sirf 70 percent efficient — toh har 100 Watt jo router use karta hai, 30 extra Watt grid se khaaya ja raha hai aur waste ho raha hai. Is paper mein Switch network mein yahi problem mili."

---

### Q3: "80 Plus standard kya hota hai?"

**Jawab (M. Umair):**
> "80 Plus 2004 mein introduce hua ek certification program hai jo PSU manufacturers ke liye hai. Basic requirement yeh thi ke PSU 20%, 50%, aur 100% load pe kam az kam 80% efficient honi chahiye. Phir is standard ko extend kiya gaya — Bronze, Silver, Gold, Platinum, aur Titanium tak — har level pe higher efficiency requirements hain.
>
> Titanium sabse acha hai — 50% load pe 96% efficiency required hai. Is paper mein Switch routers ke PSUs mostly Platinum level ke neeche the."

---

### Q4: "Agar traffic aur power mein correlation nahi hai — toh bijli kaise bachayein?"

**Jawab (Ahmad):**
> "Yahi is paper ka core message hai. Traditional thinking thi ke traffic kam karo — links off karo — power bachta hai. Lekin paper prove karta hai ke traffic cost negligible hai — 0.026% of total power.
>
> Asli power eaters hain: base router power, transceivers jo plugged in hain, aur PSU conversion losses. Toh savings strategies honi chahiye:
> PSUs behtar quality ki lagao — 7% savings
> Ek PSU hot stand-by pe rakho — 4% savings
> Transceivers jo unused hain unhen unplug karo — noteworthy savings
>
> Link sleeping — yani links off karna — is paper ke hisaab se sirf 0.4 se 1.9% bachata hai. Much less than expected."

---

### Q5: "Yeh experiment reproduce karna kyun mushkil tha?"

**Jawab (Umair Hafeez):**
> "Teen cheezein thin jo mushkil banati thin.
>
> Pehli — documentation incomplete thi. requirements.txt mein numpy aur scipy listed nahi the. Humne notebooks read karke khud discover kiya.
>
> Doosri — version conflict tha. Plotly 5.21 aur Kaleido 1.3 incompatible hain. Yeh error message dekhne ke baad humne research ki aur solution find kiya.
>
> Teesri — kuch data private hai — Autopower measurements aur network topology Switch ne share nahi ki. Lekin yeh researchers ne already note kiya tha paper mein. Jo public tha, woh sab reproduce ho gaya."

---

### Q6: "Paper mein kaunsa section sabse important hai aur kyun?"

**Jawab (Ahmad):**
> "Mera jawab hai Section 9 — PSU Analysis — kyunki yeh sabse actionable hai.
>
> Section 3 aur 7 basically problem diagnose karte hain — datasheets ghalat hain, traffic irrelevant hai. Lekin Section 9 ek concrete solution deta hai: better PSUs se bina kuch bhi network mein change kiye 9% energy savings possible hain. Aur yeh easily implementable hai — PSU replace karo, network same rahti hai.
>
> Research ki value is mein hai ke yeh specifically quantify karta hai — 9% — aur explain karta hai mechanism — PSU efficiency curves — taake ISPs actual decisions le sakein."

---

### Q7: "Agar paper mein numbers reproduce nahi hote toh kya hota?"

**Jawab (M. Umair):**
> "Agar numbers match na karte toh do possibilities hoti:
>
> Pehli — code ya data mein bug hai — yani original paper galat tha.
> Doosri — humara environment ya understanding galat tha.
>
> Dono cases mein humen detailed analysis karni hoti — kahan se difference aa raha hai, kis cell mein, kis variable mein. Yeh bhi valid reproduction work hota. Fortunately, hamare case mein sab kuch exactly match kiya — har number Table 1, Table 3, Table 4 mein same tha. Yeh paper ki reproducibility ki strength prove karta hai."

---

### Q8: "Yeh paper practically ISPs ke liye kya suggest karta hai?"

**Jawab (Ahmad):**
> "Paper kuch concrete suggestions deta hai:
>
> Ek — PSU monitoring improve karo. Abhi zyada tar monitoring tools sirf P-in measure karte hain. P-out bhi measure karo taake real efficiency track ho sake.
>
> Do — Jab router replace karo, better-rated PSU lagao — kam az kam Platinum.
>
> Teen — Hot stand-by feature enable karo agar router support karta hai — ek PSU chal raha ho dono ke load pe.
>
> Chaar — Transceivers jo unused ports mein hain unhen unplug karo — woh bhi power khaate hain.
>
> Yeh sab changes bina network traffic ya routing affect kiye ho sakte hain — isliye yeh low-risk, high-impact recommendations hain."

---

### Q9: "Is paper mein limitations kya hain?"

**Jawab (M. Umair):**
> "Paper khud limitations acknowledge karta hai:
>
> Pehli — Sirf ek ISP ka data hai — Switch. Doosre ISPs mein results different ho sakte hain.
>
> Doosri — Power models sirf fixed chassis routers ke liye kaam karte hain — modular routers ke liye nahi.
>
> Teesri — PSU efficiency ke liye sirf ek snapshot tha — time series nahi. Aur P-out measurements ki accuracy unclear hai.
>
> Chauthi — Link sleeping analysis mein Hypnos algorithm use hua jo assume karta hai ke transceivers off ho jaate hain — lekin yeh real-world mein nahi hota.
>
> Yeh sab limitations paper mein honestly discuss kiye gaye hain — jo good research practice hai."

---

### Q10: "Yeh paper computer science mein kyun important hai?"

**Jawab (Ahmad):**
> "Do reasons se.
>
> Pehla — Sustainability. ICT sector growing energy consumer hai. Agar hum routers ki actual power demand nahi samajhte toh Internet ko sustainable nahi bana sakte. Yeh paper ek foundation banata hai — actual data, validated models, aur concrete savings paths.
>
> Doosra — Methodology. Researchers ne jo approach use ki — external measurement se validate karna, power models derive karna, phir real network pe apply karna — yeh ek reproducible framework hai. Doosre researchers ab iska use kar sakte hain different networks pe, different routers pe.
>
> Is liye yeh paper IMC mein accept hua — ek top-tier conference — kyunki na sirf results novel hain, balke methodology aur tools bhi community ke liye contribute kiye gaye hain."

---

### Q11: "Figure 4 reproduce kyun nahi hua?"

**Jawab (Umair Hafeez):**
> "Figure 4 mein Autopower ka data hai — yeh woh external power measurements hain jo researchers ne physical hardware lagaa ke kiye the. Unhone ek Raspberry Pi aur ek special power meter milaa ke ek device banaya — Autopower — aur ise production routers ke saath lagaya.
>
> Yeh raw data — actual watt readings over time — private hai kyunki yeh Switch ISP ke actual production routers se hai. Switch ne agree kiya data share karne ke liye analysis ke liye, lekin raw measurement files public release mein nahi hain.
>
> Paper ke Section 9.2 mein clearly likha hai: 'We cannot share the source inventory and sensor data.' Toh yeh humari limitation nahi — yeh research ethics ka hissa hai."

---

### Q12: "Transceiver kya hota hai aur yeh power mein kyun matter karta hai?"

**Jawab (M. Umair):**
> "Transceiver ek pluggable module hota hai jo router ke port mein lagta hai. Yeh optical ya electrical signal ko convert karta hai taake data transmit ho sake — jaise ek LR4 optical transceiver fiber optic cable ke through data bhejta aur receive karta hai.
>
> Power mein matter karta hai isliye ke Switch network mein saare transceivers milaa ke 2.2 kilowatt consume karte hain — yani total network power ka roughly 10 percent.
>
> Aur interesting finding yeh thi ke jab aap port 'down' karte ho — yani interface disable karte ho — transceiver physically powered off nahi hota. Matlab unused port mein bhi transceiver chal raha hota hai aur power kha raha hota hai. Yeh software behavior hai jo fix kiya ja sakta hai."

---

*Presentation End.*

---

> **Tip:** Ahmad poori presentation mein narrative le chalata hai. Umair Hafeez technical slides aur terminal dikhata hai jab uski baari ho. M. Umair figures aur tables screen pe show karta hai aur numbers explain karta hai. Q&A mein jo sawaal jis ke domain ka ho, woh jawab de — lekin Ahmad overall narrative control kare.
